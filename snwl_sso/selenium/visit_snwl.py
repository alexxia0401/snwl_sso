#!/usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://10.0.0.24")

driver.switch_to_frame("authFrm")
elem = driver.find_element_by_id("userName")
elem.clear()
elem.send_keys("admin")
passwd = driver.find_element_by_name("pwd")
passwd.clear()
passwd.send_keys("password")

driver.find_element_by_name("Submit").click()
#time.sleep(2)
driver.get("https://10.0.0.24/main.html")
driver.switch_to_frame("outlookFrame")
driver.find_element_by_link_text("Users").click()
# Users > Settings
driver.find_element_by_css_selector("#pnl10 > #nav_head2 > #nav_head2_textbox > a.nav_sub_sett").click()
#driver.switch_to_frame("tabFrame")
#driver.find_element_by_id("autoLognCfgBtn").click()


time.sleep(4)
#driver.quit()
