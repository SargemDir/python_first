from selenium.webdriver.common.by import By


def test_button1_exist(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    assert driver.find_element(By.ID, 'submit-id-submit').is_displayed()

def test_button1_clicked(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    driver.find_element(By.ID, 'submit-id-submit').click()
    assert 'Submitted' == driver.find_element(By.ID, 'result-text').text