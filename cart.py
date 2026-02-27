from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver):
        self._driver = driver
        self._waiter = WebDriverWait(driver, 90)

    def get_cart(self):
        self._driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        self._waiter.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
        )
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
