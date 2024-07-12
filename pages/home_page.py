from pages.confpage import BasePage
from base.actions import Action
from locators.locators import SetHomepageLocator
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_welcome_msg(self):
        return Action(self.driver).get_text(SetHomepageLocator.msg_welcome_user)

    def is_homepage_display(self):
        return Action(self.driver).is_display(SetHomepageLocator.msg_welcome)

    def click_create_an_account_link(self):
        Action(self.driver).click(SetHomepageLocator.lnk_create_account)