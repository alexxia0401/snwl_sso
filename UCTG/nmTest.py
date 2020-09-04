#!/usr/bin/env python3

import nmap
import smtplib
from email.mime.text import MIMEText
from email.header import Header


servers = (
    "100.200.2.79",
#    "100.200.2.12",  # debug use
    "100.200.2.206",
    "100.200.2.208",
    "100.200.2.182",
    "100.200.2.38",
    "10.74.97.36",
    "10.74.97.46",
    "10.74.97.40",
    "10.74.97.43",
    "10.74.97.41",
    "100.200.2.57")

offline = []

for server in servers:
    nm = nmap.PortScanner()
    result = nm.scan(server, arguments='-sn')
    try:
        if result['scan'][server]['status']['state'] == "up":
            continue
    except:
        offline.append(server)

print(offline)

sender = 'q@c.com'
receivers = [
    'q@c.com',
    'y@c.com',    
    'z@c.com']

message = MIMEText("The following servers are down: {}".format(offline), 'plain', 'utf-8')
message['From'] = sender
message['To'] = ';'.join(receivers)

subject = 'Some CI tshark servers are down'
message['Subject'] = Header(subject, 'utf-8')

if offline:
    try:
        smtpObj = smtplib.SMTP('outbound.c.com', 25)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("Mail sent")
        smtpObj.quit()
    except smtplib.SMTPException:
        print("Error...")
else:
    print("No server offline")
