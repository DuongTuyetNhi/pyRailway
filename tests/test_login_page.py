import allure
import pytest

from models.user import User
from tests.conftest import setup_and_teardown
from pages.confpage import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.mail_page import MailPage
from pages.register_page import RegisterPage

username = "nhiagest@grr.la"
password = "12345678"
pid = "12345678"
user = User(username,password)
user_blank_us = User("", password)
user_invalid = User(username, "11111111")

@pytest.mark.usefixtures("setup_and_teardown")
@allure.title("Test Login")
class TestLogin:
    def test_login_with_blank_username(self):
        self.driver_manager.open_railway_page()
        driver = self.driver_manager.get_driver()
        base_page = BasePage(driver)
        base_page.open_login_tab()
        login_page = LoginPage(driver)
        login_page.submit_login_form(user_blank_us)
        actual_msg = login_page.get_error_msg()
        expected_msg = "There was a problem with your login and/or errors exist in your form."
        assert actual_msg == expected_msg, "The error message is not the same as expected."

    def test_login_with_valid_account(self):
        self.driver_manager.open_railway_page()
        driver = self.driver_manager.get_driver()
        base_page = BasePage(driver)
        base_page.open_login_tab()
        login_page = LoginPage(driver)
        login_page.submit_login_form(user)
        home_page = HomePage(driver)
        actual_msg = home_page.get_welcome_msg()
        expected_msg = "Welcome " + username
        assert actual_msg==expected_msg, "The welcome message is not the same as expected."

    def test_login_with_invalid_password(self):
        self.driver_manager.open_railway_page()
        driver = self.driver_manager.get_driver()
        base_page = BasePage(driver)
        base_page.open_login_tab()
        login_page = LoginPage(driver)
        login_page.submit_login_form(user_invalid)
        actual_msg = login_page.get_error_msg()
        expected_msg = "There was a problem with your login and/or errors exist in your form."
        assert actual_msg == expected_msg, "The error message is not the same as expected."

    def test_login_in_several_times(self):
        self.driver_manager.open_railway_page()
        driver = self.driver_manager.get_driver()
        base_page = BasePage(driver)
        base_page.open_login_tab()
        login_page = LoginPage(driver)

        login_page.login_several_time(user_invalid, 4)
        actual_msg = login_page.get_error_msg()
        expected_msg = "You have used 4 out of 5 login attempts. After all 5 have been used, you will be unable to login for 15 minutes."
        assert actual_msg == expected_msg, "The error message is not the same as expected."

    def test_login_in_with_inactive_account(self):
        self.driver_manager.open_mail_page()
        driver = self.driver_manager.get_driver()
        mail_page = MailPage(driver)
        mail = mail_page.get_email()
        new_user = User(mail, password, pid)

        self.driver_manager.open_railway_page()
        home_page = HomePage(driver)
        home_page.open_tab("Register")
        register_page = RegisterPage(driver)
        register_page.fill_register_form(new_user)
        register_page.click_btn_register()
        register_page.open_login_tab()

        login_page = LoginPage(driver)
        login_page.submit_login_form(new_user)
        actual_msg = login_page.get_error_msg()
        expected_msg = "Invalid username or password. Please try again."
        assert actual_msg == expected_msg, "The error message is not the same as expected."
