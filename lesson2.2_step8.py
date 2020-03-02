#!/usr/bin/env python
# coding: utf-8

# In[2]:

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Моё Имя")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Моя Фамилия")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("Мой email")
    
    file_txt = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'lesson2.2_step8.txt')           # добавляем к этому пути имя файла 
    file_txt.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
