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
    
    #page3
    textboxes =  browser.find_elements(By.CLASS_NAME,"whsOnd.zHQkBf")
    radiobuttons =  browser.find_elements(By.CLASS_NAME,"AB7Lab.Id5V1")
    linearscale =  browser.find_elements(By.CLASS_NAME,"AB7Lab.Id5V1")
    submitbutton =  browser.find_elements(By.CLASS_NAME,"NPEfkd.RveJvd.snByac")
    nextbutton = browser.find_elements(By.CLASS_NAME,"NPEfkd.RveJvd.snByac")
    
    #maths physics che bio ss eng
    radiobuttons[random.randint(6,9)].click()
    radiobuttons[random.randint(16,19)].click()
    radiobuttons[random.randint(25,29)].click()
    radiobuttons[random.randint(34,39)].click()
    radiobuttons[random.randint(44,47)].click()
    radiobuttons[random.randint(55,58)].click()
    
    #b c10 60-62, bc12 63 - 65
    radiobuttons[random.randint(60,61)].click()
    radiobuttons[63].click()
    radiobuttons[random.randint(66,69)].click()
    radiobuttons[random.randint(76,77)].click()
    radiobuttons[random.randint(78,79)].click()
    radiobuttons[83].click()
    radiobuttons[random.randint(93,97)].click()
    nextbutton[1].click()
    
    #page 6

    textboxes =  browser.find_elements(By.CLASS_NAME,"whsOnd.zHQkBf")
    radiobuttons =  browser.find_elements(By.CLASS_NAME,"AB7Lab.Id5V1")
    linearscale =  browser.find_elements(By.CLASS_NAME,"AB7Lab.Id5V1")
    submitbutton =  browser.find_elements(By.CLASS_NAME,"NPEfkd.RveJvd.snByac")
    nextbutton = browser.find_elements(By.CLASS_NAME,"NPEfkd.RveJvd.snByac")

    
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
