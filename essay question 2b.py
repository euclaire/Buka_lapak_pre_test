from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def input_form(form, text):
    search = driver.find_element_by_id(form)
    search.send_keys(text)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.bukalapak.com/")

#Click on Login
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sigil-header__nav"))
    )
    driver.find_element_by_link_text('Login').click()
except: 
    print("fail")


#input string to login form and login
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "new_user_session"))
    )
    input_form('user_session_username', '') #input email in function
    input_form('user_session_password', '') #input password in function
    driver.find_element_by_id('user_session_remember_me').click()
    driver.find_element_by_class_name('c-btn--spinner__icon').click()
except:
    print("fail on login form")
