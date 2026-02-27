from selenium.webdriver.common.by import By


class Main:
    def __init__(self, driver):
        self._driver = driver

    def buy(self, product):
        self._driver.find_element(By.CSS_SELECTOR, product).click()

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR,
                                  "a.shopping_cart_link").click()
