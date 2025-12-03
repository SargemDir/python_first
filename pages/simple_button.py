from pages.base_page import BasePage

button_selector = ()

class SimpleButtonPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def button(self):
        return self.find()
