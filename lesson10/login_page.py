import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Магазин одежды")
class Login:
    def __init__(self, driver):
        self._driver = driver
        self._waiter = WebDriverWait(driver, 90)

    @allure.step("Перейти на страницу авторизации по ссылке")
    def get_login_page(self):
        """ Метод позволяет перейти на страницу авторизации по ссылке"""
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Произвести авторизацию по логин:{login} и пароль:{password}")
    def autorization(self, login: str, password: str):
        """ Метод позволяет авторизироваться
        с данными, принимаемыми в аргументы"""
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#login-button").click()
        self._waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.title"))
            )
