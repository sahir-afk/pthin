from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()                                       #says what browser to use
driver.maximize_window()                                                                    
driver.get("https://www.news.google.com")
top_stories = driver.find_element(By.LINK_TEXT, "Top stories")
top_stories.click()
time.sleep(3)
headlines = driver.find_elements(By.CLASS_NAME, "gPFEn")
with open("headlines.txt", "w+") as h:
    for headline in headlines:
        h.write(headline.text+ "\n")
        h.write("\n")
    
driver.close()