#!/usr/bin/env python
# coding: utf-8

# In[2]:

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector(".form-control")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    time.sleep(1)

finally:
    time.sleep(15)
    browser.quit()
