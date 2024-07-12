from pages.confpage import BasePage
from models.user import User
from selenium.webdriver.common.by import By
from base.driver_management import DriverManagement
from base.actions import Action
from locators.locators import SetLoginPageLocator


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def submit_login_form(self, user):
        Action(self.driver).enter(SetLoginPageLocator.txt_username, user.get_username())
        Action(self.driver).enter(SetLoginPageLocator.txt_password, user.get_password())
        Action(self.driver).scroll_to_view(SetLoginPageLocator.btn_login)
        Action(self.driver).click(SetLoginPageLocator.btn_login)

    def get_error_msg(self):
        return Action(self.driver).get_text(SetLoginPageLocator.msg_error)

    def login_several_time(self, user, times):
        for i in range(1,times+1):
            self.submit_login_form(user)

    def click_forgot_password(self):
        Action(self.driver).click(SetLoginPageLocator.lnk_forgot_password)

    def fill_reset_password_form(self, new_password, confirm_password):
        Action(self.driver).enter(SetLoginPageLocator.txt_new_password, new_password)
        Action(self.driver).enter(SetLoginPageLocator.txt_confirm_password, confirm_password)

    def click_reset_password_btn(self):
        Action(self.driver).click(SetLoginPageLocator.btn_reset_password)

    def is_token_displayed(self) -> bool:
        by, value = SetLoginPageLocator.txt_password_reset_token
        tokens = self.driver.find_elements(by, value)
        return len(tokens) != 0


    def get_reset_msg(self):
        Action(self.driver).get_text(SetLoginPageLocator.msg_reset)

    def get_confirm_password_msg(self):
        Action(self.driver).get_text(SetLoginPageLocator.msg_confirm_password)