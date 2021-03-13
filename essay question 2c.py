from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def input_form(form, text):
    search = driver.find_element_by_id(form)
    search.send_keys(text)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.bukalapak.com/")

# Click on login
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sigil-header__nav"))
    )
    driver.find_element_by_link_text('Login').click()
except: 
    print("fail on login click")


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

#Click to drop down Kategori Barang
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//p[@class='sigil-header__nav-action bl-text bl-text--body-small bl-text--semi-bold' and text() = 'Kategori barang']"))).click()

#Click on Gembok Category
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='bl-link' and @href = '/c/sepeda/equipment-tools/gembok?from=nav_header']"))).click()


# select item from catalog base on array
try:    
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='bl-flex-container flex-wrap is-gutter-16']"))
    )
    list_of_class = driver.find_elements_by_xpath("//p[@class= 'bl-text bl-text--body-small bl-text--ellipsis__2']")
    list_of_class[0].click()
except: 
    print('fail to found')
    
#click add to cart
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='c-main-product__action__cart bl-button bl-button--outline bl-button--medium']"))).click()

#click lihat keranjang
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='c-cart-dialog__cart-button c-btn c-btn--default c-btn--default c-btn--default']"))).click()
