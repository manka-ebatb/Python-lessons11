import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Магазин одежды")
class Cart:
    def __init__(self, driver):
        self._driver = driver
        self._waiter = WebDriverWait(driver, 90)

    @allure.step("Перейти в корзину по ссылке")
    def get_cart(self):
        """ Метод позволяет переходить в корзину по ссылке"""
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Перейти из корзины к заполнению данных")
    def checkout(self):
        """ Метод позволяет перейти из корзины к заполнению данных"""
        self._waiter.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
        )
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
