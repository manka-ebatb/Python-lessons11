from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/inputs")
search = driver.find_element(By.CSS_SELECTOR, "input")
search.send_keys("Sky")
search.clear()
search.send_keys("Pro")

driver.quit()
