import allure
import pytest

from models.user import User
from tests.conftest import setup_and_teardown
from pages.confpage import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.mail_page import MailPage
from pages.register_page import RegisterPage
from base.soft_assert import SoftAssert

username = "nhiagest@grr.la"
password = "12345678"
pid = "12345678"
new_username = "hellopython@grr.la"
old_user = User(username,password, pid)
new_user = User(new_username,"","")

@pytest.mark.usefixtures("setup_and_teardown")
@allure.title("Test Register")
class TestRegister:
    def test_register_with_email_has_been_used(self):
        self.driver_manager.open_railway_page()
        driver = self.driver_manager.get_driver()
        base_page = BasePage(driver)
        base_page.open_tab("Register")
        register_page = RegisterPage(driver)
        register_page.fill_register_form(old_user)
        register_page.click_btn_register()
        actual_msg = register_page.get_error_msg()
        expected_msg = "This email address is already in use."
        assert actual_msg == expected_msg, "The actual message is not the same as expected."

    @allure.description("User can't create account while password and PID fields are empty")
    def test_register_with_blank_fields(self):
        self.driver_manager.open_railway_page()
        driver = self.driver_manager.get_driver()
        base_page = BasePage(driver)
        base_page.open_tab("Register")
        register_page = RegisterPage(driver)
        register_page.fill_register_form(new_user)
        register_page.click_btn_register()

        soft_assert = SoftAssert()

        actual_msg = register_page.get_error_msg()
        expected_msg = "There're errors in the form. Please correct the errors and try again."
        soft_assert.check(actual_msg == expected_msg, "The actual message is not the same as expected.")

        password_actual_msg = register_page.get_validation_password_error()
        password_expected_msg = "Invalid password length."
        soft_assert.check(password_actual_msg == password_expected_msg,
                          "The actual password message is not the same as expected.")

        pid_actual_msg = register_page.get_validation_pid_error()
        pid_expected_msg = "Invalid ID length."
        soft_assert.check(pid_actual_msg == pid_expected_msg,
                          "The actual pid message is not the same as expected.")

        soft_assert.assert_all()

    def test_register_account(self):
        self.driver_manager.open_mail_page()
        driver = self.driver_manager.get_driver()
        mail_page = MailPage(driver)
        mail = mail_page.get_email()
        user = User(mail, password, pid)
        mail_window = self.driver_manager.get_current_tab()
        self.driver_manager.open_new_tab()

        self.driver_manager.open_railway_page()
        home_page = HomePage(driver)
        home_page.click_create_an_account_link()
        railway_window = self.driver_manager.get_current_tab()
        register_page = RegisterPage(driver)
        register_page.fill_register_form(user)
        register_page.click_btn_register()
        register_page.is_msg_register_displayed()
        self.driver_manager.switch_to_tab(mail_window)
        driver.refresh()

        before = self.driver_manager.get_current_tabs()

        mail_page.confirm_account()

        after = self.driver_manager.get_current_tabs()

        self.driver_manager.switch_to_new_tab(before, after)

        assert register_page.is_confirm_msg_register_displayed()

        register_page.open_login_tab()
        login_page = LoginPage(driver)
        login_page.submit_login_form(user)



