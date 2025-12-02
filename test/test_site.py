import time

from pages.homePage import HomePage
from pages.product import ProductPage

#main_page_link = 'https://demoblaze.com/index.html'


def test_open_s6(driver):

    home_page = HomePage(driver)
    home_page.open()
    home_page.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')


def test_two_monitors(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_monitor()
    time.sleep(3)
    home_page.check_that_products_count(2)

