from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
username = driver.find_element(By.CSS_SELECTOR, "#username")
password = driver.find_element(By.CSS_SELECTOR, "#password")
logIn = driver.find_element(By.CSS_SELECTOR, ".fa-2x")
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
logIn.click()
info = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(info)
driver.quit()
