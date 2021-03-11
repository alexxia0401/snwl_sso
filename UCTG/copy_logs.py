#!/usr/bin/env python3

import re
import subprocess


def read_logs():
    OLD_TXT = 'old.txt'
    NEW_TXT = 'new.txt'
    READ_FILE = 'latest'

    old_obj = open(OLD_TXT, 'r')
    old_log = old_obj.readline()
    old_obj.close()
    print("old value is:", old_log)

    new_obj = open(NEW_TXT, 'w')
    subprocess.run(f'ls -l {READ_FILE}', shell=True, stdout=new_obj)
    new_obj.close()

    new_obj = open(NEW_TXT, 'r')
    new_res = new_obj.readline()
    new_obj.close()

    # lrwxrwxrwx 1 root root 15 Jan 27 08:05 latest -> 20210127-080552

    new_log = re.findall(r'->.*', new_res)
    new_log = new_log[0]
    new_log = new_log[3:]
    print("new value is:", new_log)

    if old_log  == new_log:
        return "equal", new_log
    else:
        old_obj = open(OLD_TXT, 'w')
        old_obj.write(new_log)
        old_obj.close()
        return "unequal", new_log

def send_logs():
    res, new_log = read_logs()

    if res == 'equal':
        print('old and new value is equal, do nothing...')
    else:
        try:
            print('scp new logs to 102 server...')
            subprocess.run(f"expect -c 'spawn scp -r {new_log} " + "root" + "@" + "10.75.185.102" + ":/home/e2elog/.;expect password;send \"" + "pswd1234" + "\r\";interact'", shell=True)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    send_logs()
