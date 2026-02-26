from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testing():
    driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

    driver.get("https://www.saucedemo.com/")
    waiter = WebDriverWait(driver, 90)
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span.title"))
    )
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    waiter.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
    )
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"#first-name"))
    )
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Name")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Surname")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("0000")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    
    s = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    assert s == "Total: $58.29"


    driver.quit()
