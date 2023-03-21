from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# email + pass
email = ""
password = ""
# opens outlook on chrome
driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options) 
driver.get("https://outlook.com")
driver.maximize_window()
# finds sign in button
sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_btn.click()
# finds email slot and enters email
email_slot = driver.find_element(By.NAME, "loginfmt")
email_slot.send_keys(email)
email_slot.send_keys(Keys.ENTER)
time.sleep(2)
# finds password slot and enters info
pass_slot = driver.find_element(By.XPATH, "//*[@id='i0118']")
pass_slot.send_keys(password)
pass_slot.send_keys(Keys.ENTER)
