from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By

option  = webdriver.ChromeOptions()
#option.add_argument("-incognito")

browser = webdriver.Chrome(executable_path='C:\\Users\\Desktop\\Projects\\Python\\AutoForms\\chromedriver.exe', options = option)
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSe2Yagqm8HIi_UTVG1eUyDoCMJSyrwUnr9-G2s/viewform")
count = 1
while(count<30):
    count += 1
    textboxes =  browser.find_elements(By.CLASS_NAME,"whsOnd.zHQkBf")
    radiobuttons =  browser.find_elements(By.CLASS_NAME,"AB7Lab.Id5V1")
    checkboxes =  browser.find_elements(By.CLASS_NAME,"uHMk6b.fsHoPb")
    submitbutton =  browser.find_elements(By.CLASS_NAME,"NPEfkd.RveJvd.snByac")
    nextbutton = browser.find_elements(By.CLASS_NAME,"NPEfkd.RveJvd.snByac")

    time.sleep(1)
    #page 1

    textboxes[0].send_keys("TestUser11")
    textboxes[1].send_keys(random.randint(18,22))
    radiobuttons[random.randint(0,1)].click()
    radiobuttons[4].click()
    checkboxes[0].click()
    nextbutton[0].click()
    
    #page 8

    textboxes =  browser.find_elements(By.CLASS_NAME,"whsOnd.zHQkBf")
    radiobuttons =  browser.find_elements(By.CLASS_NAME,"AB7Lab.Id5V1")
    linearscale =  browser.find_elements(By.CLASS_NAME,"AB7Lab.Id5V1")
    submitbutton =  browser.find_elements(By.CLASS_NAME,"NPEfkd.RveJvd.snByac")
    nextbutton = browser.find_elements(By.CLASS_NAME,"NPEfkd.RveJvd.snByac")

    radiobuttons[0].click()
    radiobuttons[random.randint(2,3)].click()
    radiobuttons[random.randint(4,8)].click()
    radiobuttons[random.randint(9,11)].click()
    radiobuttons[12].click()
    radiobuttons[random.randint(14,15)].click()
    #range 16-25
    radiobuttons[random.randint(21,25)].click()
    radiobuttons[random.randint(31,34)].click()
    radiobuttons[random.randint(41,43)].click()
    radiobuttons[random.randint(51,54)].click()
    submitbutton[1].click()

    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSe2YagqIm8HIi_UTVG1eUyDoCMJSyrwUnr9-G2sOe1udwx6Kw/viewform")
