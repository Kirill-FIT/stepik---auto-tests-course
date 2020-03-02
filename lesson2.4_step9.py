#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет равной 100
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element_by_id('book')
    button.click()
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector(".form-control")
    input1.send_keys(y)
    
    button = browser.find_element_by_id('solve')
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()
    