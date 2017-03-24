#!/usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

elem = driver.find_element_by_id("kw")
elem.clear()
elem.send_keys("python")
search = driver.find_element_by_id("su")
search.click()

time.sleep(10)
driver.quit()
