#!/usr/bin/env python3

# Author: Qing Xia

import urllib.request

from datetime import datetime
from influxdb import InfluxDBClient

# Codestone API example
# http://10.75.185.144:8099/codestone/action/project/ci/duration?project=Mainline-3PCC-DEV&view=DailySanity-BE&start=2020-8-18&end=2020-8-19

mpp_mainline_project = 'Mainline-3PCC-DEV'

daily_view = {
    'DailySanity-AA': "AA_Sanity",
    'DailySanity-BB': "BB_Sanity",
    'DailySanity-CC': "CC_Sanity",
    'DailySanity-DD': "DD_Sanity",
    'DailySanity-EE': "EE_Sanity",
    'DailySanity-FF': "FF_Sanity",
    'DailySanity-GG': "GG_Sanity",
    'DailySanity-HH': "HH_Sanity",
    'DailySanity-II': "II_Sanity",
    'DailySanity-JJ': "JJ_Sanity"
}

url_fetch_latest = 'http://10.75.185.144:8099/codestone/action/project/ci/duration?project={project}&view={view}&start={start_date}&end={end_date}'

DB_host = '10.74.97.172'
DB_port = '8086'
DB_database_name = 'test'

def get_sanity_running_time(project, view, start_date, end_date):
    # convert byte to string
    temp = urllib.request.urlopen(url_fetch_latest.format(project=project, view=view, start_date=start_date, end_date=end_date)).read().decode()
    content = eval(temp)  # string to a real list

    load_name_list = []  # search this time execution's all load_name

    # connect to InfluxDB
    client = InfluxDBClient(host=DB_host, port=DB_port, database=DB_database_name)

    # in list, each dictionary means a job, like 3PCC_MPP_ALD_APP_Daily
    for job in content:
        job_name = job["job_name_varchar"]
        start_time = job["start_time_datetime"]
        end_time = job["end_time_datetime"]
        load_name = job["load_name"]

        # get all load_name in this time's execution
        if load_name not in load_name_list:
            load_name_list.append(load_name)

        # convert str to datetime
        start_time_dt = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end_time_dt = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

        # convert datetime to timestamp
        start_time_stamp = start_time_dt.timestamp()
        end_time_stamp = end_time_dt.timestamp()

        running_time_stamp = end_time_stamp - start_time_stamp  # each job running time

        # An INSERT statement example
        # INSERT ALD_Sanity,job_name="3PCC_ALD_APP_Weekly_1",load_name="11-3-3MPP0001-57" start_time=1234567890,end_time=2234567890,running_time=123456, time=2020/8/1

        body = [
            {
                "measurement": daily_view[view],
                "time": datetime.utcfromtimestamp(start_time_stamp),
                "tags": {
                    "job_name": job_name,
                    "load_name": load_name
                },
                "fields": {
                    "start_time": start_time_stamp,
                    "end_time": end_time_stamp,
                    "running_time": running_time_stamp
                },
            }
        ]

        job_result = client.write_points(body)

        if job_result:
            print("Write child job running time to DB successfully")
        else:
            print("Write child job running time to DB failed")

    # A model total duration is not summed by each job running_time, but latest end_time minus earliest start time,
    # calculate this for each load.
    # Then select start_time group by load_name limit 1 to get each load execute start time.
    for l in load_name_list:
        res1 = client.query("SELECT MIN(start_time) FROM {} WHERE load_name='{}'".format(daily_view[view], l))
        min_start_time = res1.raw['series'][0]['values'][0][1]

        res2 = client.query("SELECT MAX(end_time) FROM {} WHERE load_name='{}'".format(daily_view[view], l))
        max_end_time = res2.raw['series'][0]['values'][0][1]
        total_running_time = max_end_time - min_start_time

        res3 = client.query("SELECT start_time FROM {} WHERE load_name='{}' LIMIT 1".format(daily_view[view], l))
        total_start_time = res3.raw['series'][0]['values'][0][1]
        total_start_time_stamp = datetime.fromtimestamp(total_start_time)

        body = [
            {
                "measurement": "{}_Total".format(daily_view[view]),
                "time": total_start_time_stamp,
                "tags": {
                    "job_name": "{}_total".format(daily_view[view]),
                    "load_name": l
                },
                "fields": {
                    "running_time": total_running_time
                },
            }
        ]
        job_result = client.write_points(body)

        if job_result:
            print("Write job total running time to DB successfully")
        else:
            print("Write job total running time to DB failed")


if __name__ == "__main__":
    # Commented out code is for manual run and debug
    # get_sanity_running_time(mpp_mainline_project, 'DailySanity-BE', '2020-8-1', '2020-8-5')

    # for view in daily_view:
    #     for i in range(1, 31):
    #         #get_sanity_running_time(mpp_mainline_project, view, "2020-8-{}".format(i), "2020-8-{}".format(i+1))
    #         get_sanity_running_time(mpp_mainline_project, view, "2020-8-31", "2020-9-1")

    # Crontab job or Jenkins will run this script every day afternoon, date is from yesterday to today
    # Make sure linux host has correct date and time
    today = datetime.now()
    yesterday_float = today.timestamp() - 86400
    yesterday = datetime.fromtimestamp(yesterday_float)

    today_str = today.strftime("%Y-%m-%d")
    yesterday_str = yesterday.strftime("%Y-%m-%d")

    for view in daily_view:
        get_sanity_running_time(mpp_mainline_project, view, yesterday_str, today_str)
