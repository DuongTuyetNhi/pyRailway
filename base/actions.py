from selenium.webdriver.common.by import By
class Action:
    def __init__(self, driver):
        self.driver = driver

    def enter(self, by_element, information):
        by, value = by_element
        self.driver.find_element(by, value).send_keys(information)

    def click(self, element):
        by, value = element
        self.driver.find_element(by, value).click()

    def scroll_to_view(self, element):
        by, value = element
        ele = self.driver.find_element(by, value)
        ele.location_once_scrolled_into_view

    def get_text(self, element):
        by, value = element
        return self.driver.find_element(by, value).text

    def is_display(self, element):
        by, value = element
        return self.driver.find_element(by, value).is_displayed
