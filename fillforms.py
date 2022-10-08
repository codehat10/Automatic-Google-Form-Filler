from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By

option  = webdriver.ChromeOptions()
#option.add_argument("-incognito")

browser = webdriver.Chrome(executable_path='C:\\Users\\Desktop\\Projects\\Python\\AutoForms\\chromedriver.exe', options = option)
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSe2Yagqm8HIi_UTVG1eUyDoCMJSyrwUnr9-G2s/viewform")
count = 1
