#!/usr/bin/python3

from selenium import webdriver
import time

driver = webdriver.Firefox()
firstUrl = 'https://www.baidu.com'
secondUrl = 'https://news.baidu.com'

print('visit first URL')
driver.get(firstUrl)

time.sleep(3)

print('visit second URL')
driver.get(secondUrl)

time.sleep(3)
print('back to first URL')
driver.back()

print('forward to second URL')
time.sleep(3)
driver.forward()
time.sleep(3)

driver.quit()
