from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc import Calculator


def test():
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    calculator = Calculator(driver)
    calculator.get()
    calculator.timing("45")
    calculator.key(0)
    calculator.summary()
    calculator.key(1)
    calculator.answer()
    res = calculator.answer()
    assert res == "15"
    driver.quit()
