from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_cap = {
  "deviceName": "emulator-5554",
  "platformName": "android",
  "appPackage": "com.loginmodule.learning",
  "appActivity": ".activities.LoginActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'com.loginmodule.learning:id/textViewLinkRegister'))).click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'com.loginmodule.learning:id/textInputEditTextName'))).send_keys("n7")
driver.press_keycode(66)
driver.find_element_by_id("com.loginmodule.learning:id/textInputEditTextEmail").send_keys("n7")
driver.press_keycode(66)
driver.find_element_by_id("com.loginmodule.learning:id/textInputEditTextPassword").send_keys("asdasd12")
driver.press_keycode(66)
driver.find_element_by_id("com.loginmodule.learning:id/textInputEditTextConfirmPassword").send_keys("asdasd12")
driver.press_keycode(66)
driver.find_element_by_id("com.loginmodule.learning:id/appCompatButtonRegister").click()