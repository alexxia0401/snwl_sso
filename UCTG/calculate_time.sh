#!/bin/bash

start_time=`date --date='0 days ago' "+%Y-%m-%d %H:%M:%S"`
echo "start time: ${start_time}"
sleep 5
end_time=`date --date='0 days ago' "+%Y-%m-%d %H:%M:%S"`
echo "end time: ${end_time}"
duration=$(($(($(date +%s -d "$end_time")-$(date +%s -d "$start_time")))))
d_time=$(date -d@${duration} -u +%H:%M:%S)
echo "Running time: ${d_time}"