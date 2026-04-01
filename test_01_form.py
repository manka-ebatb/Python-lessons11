
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testing():
    driver = webdriver.Edge(service=EdgeService
                        (EdgeChromiumDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    waiter = WebDriverWait(driver, 7)
    driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    waiter.until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "[type='submit']"))
    )
    elements = ["#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city",
                "#country", "#job-position", "#company"]
    for element in elements:
      q = driver.find_element(By.CSS_SELECTOR, {element}).get_attribute("class")
      assert q == "alert py-2 alert-success"

    q = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert q == "alert py-2 alert-danger"


    driver.quit()

