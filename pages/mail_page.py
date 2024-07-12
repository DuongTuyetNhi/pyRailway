from pages.confpage import BasePage
from base.actions import Action
from locators.locators import SetMailPageLocator
from base.driver_management import DriverManagement

class MailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_email(self):
        Action(self.driver).click(SetMailPageLocator.cbx_scramble_address)
        return Action(self.driver).get_text(SetMailPageLocator.txt_email)

    def confirm_account(self):
        BasePage(self.driver).wait_for_element_visible(SetMailPageLocator.txt_email_confirm, 25)
        Action(self.driver).click(SetMailPageLocator.txt_email_confirm)

        BasePage(self.driver).wait_for_element_visible(SetMailPageLocator.txt_link_confirm, 25)
        Action(self.driver).click(SetMailPageLocator.txt_link_confirm)

    def login_to_email(self, mail_name, domain_name):
        Action(self.driver).click(SetMailPageLocator.btn_mail)
        Action(self.driver).enter(SetMailPageLocator.txt_mail_name, mail_name)
        Action(self.driver).click(SetMailPageLocator.btn_set)
        Action(self.driver).enter(SetMailPageLocator.slt_domain_name, domain_name)

    def reset_password(self):
        BasePage(self.driver).wait_for_element_visible(SetMailPageLocator.txt_email_reset, 25)
        Action(self.driver).click(SetMailPageLocator.txt_email_reset)
        BasePage(self.driver).wait_for_element_visible(SetMailPageLocator.txt_link_reset, 25)
        Action(self.driver).click(SetMailPageLocator.txt_link_reset)