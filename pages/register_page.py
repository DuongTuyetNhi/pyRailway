from pages.confpage import BasePage
from models.user import User
from selenium.webdriver.common.by import By
from base.driver_management import DriverManagement
from base.actions import Action
from locators.locators import SetRegisterLocator
class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_register_form(self, user):
        Action(self.driver).enter(SetRegisterLocator.txt_email, user.get_username())
        Action(self.driver).enter(SetRegisterLocator.txt_password, user.get_password())
        Action(self.driver).enter(SetRegisterLocator.txt_confirm_password, user.get_password())
        Action(self.driver).enter(SetRegisterLocator.txt_pid, user.get_pid())

    def click_btn_register(self):
        Action(self.driver).scroll_to_view(SetRegisterLocator.btn_register)
        Action(self.driver).click(SetRegisterLocator.btn_register)

    def get_error_msg(self):
        return Action(self.driver).get_text(SetRegisterLocator.msg_error)

    def get_validation_password_error(self):
        password_error = By.XPATH, SetRegisterLocator.lbl_validation_error % "password"
        return Action(self.driver).get_text(password_error)

    def get_validation_pid_error(self):
        password_error = By.XPATH, SetRegisterLocator.lbl_validation_error % "pid"
        return Action(self.driver).get_text(password_error)

    def is_msg_register_displayed(self):
        return Action(self.driver).is_display(SetRegisterLocator.msg_success)

    def is_confirm_msg_register_displayed(self):
        return Action(self.driver).is_display(SetRegisterLocator.msg_confirm_success)