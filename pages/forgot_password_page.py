from pages.confpage import BasePage
from base.actions import Action
from locators.locators import SetForgotPasswordPage

class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email_address(self, email):
        Action(self.driver).enter(SetForgotPasswordPage.txt_email, email)

    def click_send_instruction_btn(self):
        Action(self.driver).click(SetForgotPasswordPage.btn_send)