from selenium import webdriver
import time

PATH="/Users/adambons/selenium/webdrivers/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("https://google.com")
time.sleep(5)
driver.get("https://example.com")
driver.quit()