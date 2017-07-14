#!/usr/bin/python3

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://m.mail.10086.cn')

driver.set_window_size(480, 800)

time.sleep(10)
driver.quit()
