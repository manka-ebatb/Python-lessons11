from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver):
        self._driver = driver
        self._waiter = WebDriverWait(driver, 90)

    def get_login_page(self):
        self._driver.get("https://www.saucedemo.com/")

    def autorization(self, login, password):
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#login-button").click()
        self._waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.title"))
            )
