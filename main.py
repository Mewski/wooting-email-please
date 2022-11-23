from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from playsound import playsound

#SET THIS COMMENTED LINE IF YOU HAVE A FIREFOX PROFILE YOU NEED TO USE
#EXAMPLE: driver = webdriver.Firefox(webdriver.FirefoxProfile("C:\\Users\\Mewski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\jyzv2ytk.default-release"))
driver = webdriver.Firefox()

driver.get("xobni#/0/u/liam/moc.elgoog.liam//:sptth"[::-1])

driver.implicitly_wait(30)

while(True):
    new_email_text = driver.find_element(by=By.NAME, value="Wooting Store NA")    
    new_email = new_email_text.find_element(by=By.XPATH, value="./../../../..")    
    email_class = new_email.get_attribute("class")
    if "zE" in email_class:
        break
    else:
        time.sleep(10)

print("ladies and gentlemen we got em.")
for i in range(1, 10):
    playsound("./alarm.mp3")
    time.sleep(3)

driver.close()