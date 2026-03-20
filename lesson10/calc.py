import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Калькулятор")
class Calculator:
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self._driver = driver
        self._waiter = WebDriverWait(driver, 90)

    @allure.step("Перейти на страницу с калькулятором")
    def get(self):
        """ Метод позволяет перейти на страницу с калькулятором """
        self._driver.get(self.url)

    @allure.step("Установить задержку на ответ {t} секунд")
    def timing(self, t: int):
        """ Метод позволяет установить задержку в ответе калькулятора
        в количестве секунд, равном аргументу t"""
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(t)

    @allure.step("Нажать на кнопку с индексом {k}")
    def key(self, k: int):
        """ Метод позволяет нажимать на кнопку с индексом равным аргументу k"""
        key = self._driver.find_elements(By.CSS_SELECTOR,
                                         "span.btn-outline-primary")
        key[k].click()

    @allure.step("Нажать на кнопку '+'")
    def summary(self):
        """ Метод позволяет нажимать на кнопку сложения"""
        operator = self._driver.find_elements(By.CSS_SELECTOR, "span.operator")
        operator[0].click()

    @allure.step("Нажать на кнопку '='")
    def answer(self) -> str:
        """ Метод позволяет нажимать на кнопку
        для получения результата вычислений"""
        self._driver.find_element(By.CSS_SELECTOR,
                                  "span.btn-outline-warning").click()
        self._waiter.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                "span#spinner"))
        )
        res = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return res
