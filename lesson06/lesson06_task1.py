from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
waiter = WebDriverWait(driver, 16)
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
button.click()
waiter.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)
print(driver.find_element(By.CSS_SELECTOR, "p.bg-success").text)
driver.quit()
