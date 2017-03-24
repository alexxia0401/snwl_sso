#!/usr/bin/python3

import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

print('maximize window')
driver.maximize_window()

time.sleep(10)
driver.quit()
