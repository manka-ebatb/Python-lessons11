from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
waiter = WebDriverWait(driver, 90)
driver.find_element(By.CSS_SELECTOR, "#delay").clear()
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
Keys.ENTER
key = driver.find_elements(By.CSS_SELECTOR, "span.btn-outline-primary")
operator = driver.find_elements(By.CSS_SELECTOR, "span.operator")
key[0].click()
operator[0].click()
key[1].click()
driver.find_element(By.CSS_SELECTOR, "span.btn-outline-warning").click()
waiter.until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR, "span#spinner"))
)


def testing():
    res = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    assert res == "15"


driver.quit()
