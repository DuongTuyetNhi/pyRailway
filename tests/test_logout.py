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
user = User(username,password)

@pytest.mark.usefixtures("setup_and_teardown")
@allure.title("Test Logout")
class TestLogout:
    def test_logout(self):
        self.driver_manager.open_railway_page()
        driver = self.driver_manager.get_driver()
        base_page = BasePage(driver)
        base_page.open_login_tab()
        login_page = LoginPage(driver)
        login_page.submit_login_form(user)
        home_page = HomePage(driver)
        home_page.open_tab("Log out")

        home_page.is_homepage_display()
        home_page.is_logout_tab_present()
        