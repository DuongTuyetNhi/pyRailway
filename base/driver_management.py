import configparser
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.by import By

class DriverManagement:
    def __init__(self):
        config = configparser.ConfigParser()
        config_file_path = os.path.abspath(r'..\properties.ini')
        config.read(config_file_path)

        self.railway_url = config.get('DEFAULT', 'railway_url')
        self.email_url = config.get('DEFAULT', 'email_url')
        self.browser = config.get('DEFAULT', 'browser')
        self.runMode = config.get('DEFAULT', 'runMode')
        self.remoteUrl = config.get('DEFAULT', 'remoteUrl')
        self.driver = None

    def init_driver(self, runMode, browser):
        if runMode.lower() == 'local':
            if browser.lower() == 'chrome':
                self.driver = webdriver.Chrome(service=ChromeService())
            elif browser.lower() == 'firefox':
                self.driver = webdriver.Firefox(service=FirefoxService())
            else:
                self.driver = webdriver.Chrome(service=ChromeService())
        elif runMode.lower() == 'grid':
            if browser.lower() == 'chrome':
                chrome_options = ChromeOptions()
                self.driver = webdriver.Remote(command_executor=self.remoteUrl, options=chrome_options)
            elif browser.lower() == 'firefox':
                firefox_options = FirefoxOptions()
                self.driver = webdriver.Remote(command_executor=self.remoteUrl, options=firefox_options)
            else:
                chrome_options = ChromeOptions()
                self.driver = webdriver.Remote(command_executor=self.remoteUrl, options=chrome_options)

    def get_driver(self):
        return self.driver

    def open_railway_page(self):
        retry_count = 5
        retry = 0
        while retry < retry_count:
            try:
                self.driver.get(self.railway_url)
                if "Safe Railway" in self.driver.title:
                    break
            except Exception as e:
                print("Failed to load")
            retry += 1

    def open_mail_page(self):
        self.driver.get(self.email_url)

    def get_current_tab(self):
        return self.driver.current_window_handle

    def get_current_tabs(self):
        return self.driver.window_handles

    def open_new_tab(self):
        self.driver.execute_script("window.open('');")
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        return new_tab

    def switch_to_tab(self, tab_handle):
        self.driver.switch_to.window(tab_handle)
        self.current_tab = tab_handle

    def switch_to_new_tab(self, before_tabs, after_tabs):
        new_tab = list(set(after_tabs) - set(before_tabs))
        if new_tab:
            new_tab_handle = new_tab[0]
            self.driver.switch_to.window(new_tab_handle)
            return new_tab_handle
        else:
            raise Exception("No new tab opened")

    def get_screenshot_as_png(self):
        return self.driver.get_screenshot_as_png()