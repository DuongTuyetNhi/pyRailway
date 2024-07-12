from selenium.webdriver.common.by import By
from base.driver_management import DriverManagement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_tab = "//div[@id='menu']//li/a[span[text()='%s']]"
        self.tabs = {}
        self.current_tab = driver.current_window_handle
        self.tabs[self.current_tab] = 'original_tab'

    def get_driver(self):
        return self.driver

    def get_tab_element(self, tab):
        by_tab = By.XPATH, self.menu_tab % tab
        return self.driver.find_element(*by_tab)

    def open_tab(self, tab):
        self.get_tab_element(tab).click()

    def open_login_tab(self):
        self.get_tab_element("Login").click()

    def is_logout_tab_present(self) -> bool:
        tab_logout = By.XPATH, self.menu_tab % "Log out"
        elements = self.driver.find_elements(*tab_logout)
        return bool(elements) and elements[0].is_displayed()

    def wait_for_element_visible(self, element, timeout):
        # wait = WebDriverWait(self.driver, 10)
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))
