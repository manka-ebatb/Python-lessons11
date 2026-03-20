import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Магазин одежды")
class Checkout:
    def __init__(self, driver):
        self._driver = driver
        self._waiter = WebDriverWait(driver, 90)

    @allure.step("Заполнить форму с данными {fname}, {lname}, {code}")
    def complete_form(self, fname: str, lname: str, code: int):
        """ Метод позволяет заполнить форму с
        данными, принимаемые в аргументы"""
        self._waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#first-name"))
            )
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#first-name").send_keys(fname)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#last-name").send_keys(lname)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#postal-code").send_keys(code)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#continue").click()

    @allure.step("Получить общую сумму покупки")
    def get_total(self) -> str:
        """ Метод позволяет получить общую сумму покупки"""
        res = self._driver.find_element(By.CSS_SELECTOR,
                                        "div.summary_total_label").text
        return res
