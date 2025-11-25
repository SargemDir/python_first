from itertools import count

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

main_page_link = 'https://demoblaze.com/index.html'

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()


def test_open_s6(driver):
    driver.get(main_page_link)
    galaxy_s6 = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'

def test_two_monitors(driver):
    driver.get(main_page_link)
    monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(3)
    monitors = driver.find_elements(By.CSS_SELECTOR, '.card')
    assert  len(monitors) == 2
