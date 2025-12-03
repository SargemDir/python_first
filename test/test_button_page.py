from selenium.webdriver.common.by import By
from pages.simple_button import SimpleButtonPage


def test_button1_exist(driver):
    simple_page = SimpleButtonPage(driver)
    simple_page.open()
    assert simple_page.button_is_displayed()

def test_button1_clicked(driver):
    simple_page = SimpleButtonPage(driver)
    simple_page.open()
    simple_page.click_button()
    assert 'Submitted' == simple_page.result_text()