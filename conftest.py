import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='module')
def driver():
    #options = Options()
    #options.add_argument('--headless')
    #driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()