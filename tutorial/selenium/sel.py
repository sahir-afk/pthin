from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)

# driver.get("https://inventwithpython.com")
# link_elem = driver.find_element(By.LINK_TEXT, "Read Online for Free")
# link_elem.click()

driver.get("https://school.district196.org/home")
username = driver.find_element(By.ID, "edit-mail")
username.send_keys("797879")

password = driver.find_element(By.NAME, "pass")
password.send_keys("pagey08")

password.send_keys(Keys.RETURN)
time.sleep(1)

html = driver.find_element(By.TAG_NAME, "html")
html.send_keys(Keys.END)
time.sleep(1)
html.send_keys(Keys.HOME)