import time

import allure
import pytest

from base.soft_assert import SoftAssert
from models.user import User
from tests.conftest import setup_and_teardown
from pages.confpage import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.mail_page import MailPage
from pages.register_page import RegisterPage
from pages.forgot_password_page import ForgotPasswordPage

username = "nhiagest@grr.la"
password = "12345678"
pid = "12345678"
user = User(username,password)
str = username.split("@")
mail_name = str[0]
domain_name = str[1]
user_blank_us = User("", password)
user_invalid = User(username, "11111111")

@pytest.mark.usefixtures("setup_and_teardown")
@allure.title("Test Forgot password")
class TestForgotPassword:
    def test_reset_password_same_old_password(self):
        self.driver_manager.open_railway_page()
        driver = self.driver_manager.get_driver()
        base_page = BasePage(driver)
        railway_window = self.driver_manager.get_current_tab()
        base_page.open_login_tab()
        login_page = LoginPage(driver)
        login_page.click_forgot_password()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email_address(username)
        forgot_password_page.click_send_instruction_btn()
        self.driver_manager.open_new_tab()

        self.driver_manager.open_mail_page()
        mail_page = MailPage(driver)
        mail_window = self.driver_manager.get_current_tab()
        mail_page.login_to_email(mail_name, domain_name)
        before = self.driver_manager.get_current_tabs()

        mail_page.reset_password()

        after = self.driver_manager.get_current_tabs()

        self.driver_manager.switch_to_new_tab(before, after)
        soft_assert = SoftAssert()
        soft_assert.check(login_page.is_token_displayed(), "Token is not display")
        login_page.fill_reset_password_form(password, password)
        login_page.click_reset_password_btn()

        actual_msg = login_page.get_reset_msg()
        expected_msg = "The new password cannot be the same with the current password"
        soft_assert.check(actual_msg == expected_msg, "The actual message is not the same as expected.")
        soft_assert.assert_all()
