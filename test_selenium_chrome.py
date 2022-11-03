from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")
time.sleep(5)
driver.get("https://example.com")
driver.quit()