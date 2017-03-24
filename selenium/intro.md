#### 预先条件
* 有一定 linux 基础
* 有一定 python 编程基础
* 本教程基于 selenium3 + python3
* 环境 ubuntu 16.04

#### How to install selenium module in Ubuntu
```bash
apt-get install python3-pip
pip3 install selenium
```

#### 如何查看 selenium 版本
```bash
#python3
```
```python
>>> import selenium
>>> help(selenium)

VERSION
    3.3.1
```

#### 下载 firefox 驱动
https://github.com/mozilla/geckodriver/releases  
目前 2017/3 版本为 0.15
```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.15.0/geckodriver-v0.15.0-linux64.tar.gz
tar -xzvf geckodriver-v0.15.0-linux64.tar.gz
root@alex-ubuntu:~/sso/selenium# ll geckodriver
-rwxrwxr-x 1 alex alex 6580458 3月   8 19:39 geckodriver*
# 把驱动添加进 PATH
export PATH=$PATH:/root/sso/selenium
echo $PATH # 确认 driver 路径已在 PATH 中
```

#### 一个简单的例子，访问百度主页并搜索关键字 python
```bash
# 在 Ubuntu terminal 中执行以下代码
save as visit_baidu.py
chmod a+x ./visit_baidu.py
./visit_baidu.py
# 脚本会自动调用 firefox，打开 baidu 主页输入 python 并搜索。
```

```bash
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
```

#### 自动登录 SonicOS
执行以下代码，把 10.0.0.24 替换成你自己盒子的 WAN IP。
```
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

time.sleep(10)
driver.quit()
```

好了，你已经入门了。剩下的就开始看官方文档吧~  
http://www.seleniumhq.org/