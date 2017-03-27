#!/usr/bin/python3

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def usage():
    print('''Usage: command WANIP
e.g. ./license.py 10.0.0.24''')

if len(sys.argv) != 2:
    usage()
    sys.exit()

url = 'https://' + sys.argv[1]

# open SonicOS
driver = webdriver.Firefox()
driver.get(url)

# login
driver.switch_to_frame("authFrm")
driver.find_element_by_id("userName").clear()
driver.find_element_by_id("userName").send_keys("admin")
driver.find_element_by_name("pwd").clear()
driver.find_element_by_name("pwd").send_keys("password")
driver.find_element_by_name("Submit").click()

# active in license page
driver.get(url + "/activationView.html")
driver.find_element_by_link_text("click here").click()
#driver.implicitly_wait(15)

elem = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_name("login"))
elem.clear()
elem.send_keys("wgong@sonicwall.com")
driver.find_element_by_name("pwd").clear()
driver.find_element_by_name("pwd").send_keys("password")
driver.find_element_by_name("Submit").click()

time.sleep(30)
#driver.quit()
