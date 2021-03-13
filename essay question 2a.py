from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

	

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.bukalapak.com/")

#Click on Daftar
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sigil-header__nav"))
    )
    driver.find_element_by_link_text('Daftar').click()
except: 
    print("fail")


#input string to regist form
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bl-text-field__input"))
    )
    search = driver.find_element_by_class_name("bl-text-field__input")
    search.send_keys("testo@gmail.com")
    search,send_keys(Keys.RETURN)
except:
    print("fail")

#click send verification code
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@class='bl-text bl-text--body-default bl-text--semi-bold bl-text--inverse']"))).click()