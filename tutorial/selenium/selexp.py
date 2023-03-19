from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)        #says what browser to use and makes it so that it doesnt close immediately after the program executes
driver.maximize_window()                                                                    
driver.get("https://www.google.com")
k = driver.find_element(By.NAME, "q")                                                       #finds html element with the name attribute "q" (which is the search bar)
k.send_keys("poopy butt")                                                                   #enters text into the element k represents
time.sleep(3)
btn = driver.find_element(By.NAME, "btnK")                                                  #finds search button with the name "btnK"
btn.send_keys(Keys.RETURN)                                                                  #presses return/enter key
# or btn.click()
time.sleep(3)
driver.close()                                                                              #closes browser







