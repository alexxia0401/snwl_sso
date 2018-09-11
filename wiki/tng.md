1. download file from http://10.74.97.172/files/cisco.ova
2. download virtualbox to your own PC
3. Open virtualbox, File -> Import Appliance, choose `cisco.ova` file.
4. login user name password and root password is `root`
5. Configure NIC to make sure network is ok by yourself.
6. `su` to root
7. confgiure `/home/3pcc_scripts/config/conf_example.tts`
example:
``` bash
# PHONE
oPhone1.device_type: bigeasy_3pcc
oPhone1.ip: 10.74.97.164


# PHONE
oPhone2.device_type: bigeasy_3pcc
oPhone2.ip: 10.74.97.166


# TFTP
tftp.device_type: Linux
tftp.ip: 10.74.51.81
tftp.ipv6: 2009:17:74:5380::87
tftp.username: cisco
tftp.password: cisco

# HTTP
http.device_type: Linux
http.ip: 10.74.51.81
http.username: cisco
http.password: cisco
```
8. configure `/home/3pcc_scripts/data/env_example.txt`
change line26 and 27, use CRDC user ID
``` bash
userID1=4085284023
userID2=4085284024
```

9. configure phones, use 3pcc bigeasy phone
Voice -> Phone -> Station Name: `arupiSSomSok`

10. run script
```
cd /home/3pcc_scripts/
tng run config/conf_example.tts common/call_control/cmCFH0001_3pcc_two_way_call.py -D '{"test_env_full_path":"./data/env_example.txt"}'
```
