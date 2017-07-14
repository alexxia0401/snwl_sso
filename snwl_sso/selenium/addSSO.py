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

submit = driver.find_element_by_name("Submit")
submit.click()

time.sleep(3)


driver.find_element_by_link_text("Users").click()
driver.find_element_by_css_selector("#pnl10 > #nav_head2 > #nav_head2_textbox > a.nav_sub_sett").click()
driver.find_element_by_id("autoLognCfgBtn").click()
driver.find_element_by_id("add-btn").click()
driver.find_element_by_id("agentHost").clear()
driver.find_element_by_id("agentHost").send_keys("192.168.10.50")
driver.find_element_by_id("agentKey").click()
driver.find_element_by_id("agentKey").clear()
driver.find_element_by_id("agentKey").send_keys("123456")
driver.find_element_by_id("confirmKey").click()
driver.find_element_by_id("confirmKey").clear()
driver.find_element_by_id("confirmKey").send_keys("123456")
driver.find_element_by_name("ApplyBtn").click()
driver.find_element_by_name("OkBtn").click()



time.sleep(10)
driver.quit()
