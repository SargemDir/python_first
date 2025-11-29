from selenium.webdriver.common.by import By


class HomePage:
    url = 'https://demoblaze.com/index.html'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_that_products_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count