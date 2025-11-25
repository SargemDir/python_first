import pytest
from selenium import webdriver

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()