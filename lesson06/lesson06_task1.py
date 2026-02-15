from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
button.click()
driver.implicitly_wait(16)
print(driver.find_element(By.CSS_SELECTOR, "p.bg-success").text)
driver.quit()
