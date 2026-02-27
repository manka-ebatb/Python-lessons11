from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout:
    def __init__(self, driver):
        self._driver = driver
        self._waiter = WebDriverWait(driver, 90)

    def complete_form(self, fname, lname, code):
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

    def get_total(self):
        res = self._driver.find_element(By.CSS_SELECTOR,
                                        "div.summary_total_label").text
        return res
