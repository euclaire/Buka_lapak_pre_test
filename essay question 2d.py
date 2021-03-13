from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.bukalapak.com/")

#Search for item
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sigil-header__nav"))
    )
    search = driver.find_element_by_id('v-omnisearch__input')
    search.send_keys('bola basket')
    search.send_keys(Keys.RETURN)
except: 
    print("fail")

