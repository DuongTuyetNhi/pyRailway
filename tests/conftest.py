import pytest
import allure
import configparser
import os
from base.driver_management import DriverManagement

# config = configparser.ConfigParser()
# config_file_path = os.path.abspath(r'..\properties.ini')
# config.read(config_file_path)

@pytest.fixture(scope='session', autouse=True)
def update_config_ini(pytestconfig):
    option = pytestconfig.getoption('option')
    value = pytestconfig.getoption('value')

    config = configparser.ConfigParser()
    #config.read('properties.ini')
    config_file_path = os.path.abspath(r'..\properties.ini')
    config.read(config_file_path)
    config['DEFAULT'][option] = value

# Thiết lập tùy chọn dòng lệnh cho pytest
def pytest_addoption(parser):
    parser.addoption("--option", action="store", default="browser", help="Option to update")
    parser.addoption("--value", action="store", default="firefox", help="New value for the option")


@pytest.fixture()
def setup_and_teardown(request):
    driver_manager = DriverManagement()
    driver_manager.init_driver()
    request.cls.driver_manager = driver_manager
    yield
    driver_manager.driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Quá trình thực hiện các bài kiểm tra
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        # Nếu bài kiểm tra thất bại, chụp ảnh màn hình
        driver_manager = item.cls.driver_manager
        allure.attach(driver_manager.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)


