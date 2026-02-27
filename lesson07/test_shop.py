from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from login_page import Login
from main_page import Main
from cart import Cart
from checkout_page import Checkout


def test():
    driver = webdriver.Firefox(service=FirefoxService
                               (GeckoDriverManager().install()))
    login = Login(driver)
    login.get_login_page()
    login.autorization("standard_user", "secret_sauce")
    main = Main(driver)
    main.buy("#add-to-cart-sauce-labs-backpack")
    main.buy("#add-to-cart-sauce-labs-bolt-t-shirt")
    main.buy("#add-to-cart-sauce-labs-onesie")
    main.go_to_cart()
    cart = Cart(driver)
    cart.checkout()
    checkout = Checkout(driver)
    checkout.complete_form("Name", "Surname", "0000")
    checkout.get_total()
    s = checkout.get_total()
    assert s == "Total: $58.29"
    driver.quit()
