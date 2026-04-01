from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self._driver = driver
        self._waiter = WebDriverWait(driver, 90)

    def get(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def timing(self, t):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(t)

    def key(self, k):
        key = self._driver.find_elements(By.CSS_SELECTOR,
                                         "span.btn-outline-primary")
        key[k].click()

    def summary(self):
        operator = self._driver.find_elements(By.CSS_SELECTOR, "span.operator")
        operator[0].click()

    def answer(self):
        self._driver.find_element(By.CSS_SELECTOR,
                                  "span.btn-outline-warning").click()
        self._waiter.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                "span#spinner"))
        )
        res = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return res
