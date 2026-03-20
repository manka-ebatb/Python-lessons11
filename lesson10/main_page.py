import allure
from selenium.webdriver.common.by import By


@allure.epic("Магазин одежды")
class Main:
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Добавить продукт с id {product} в корзину")
    def buy(self, product):
        """ Метод позволяет добавлять в корзину
        продукты с id, принимаемым в аргумент"""
        self._driver.find_element(By.CSS_SELECTOR, product).click()

    @allure.step("Перейти в корзину с помощью кнопки на главной странице")
    def go_to_cart(self):
        """ Метод позволяет перейти в корзину по кнопке"""
        self._driver.find_element(By.CSS_SELECTOR,
                                  "a.shopping_cart_link").click()
