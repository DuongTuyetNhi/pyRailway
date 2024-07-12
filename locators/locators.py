from selenium.webdriver.common.by import By

class SetMailPageLocator:
    cbx_scramble_address = (By.ID, "use-alias")
    txt_email = (By.ID, "email-widget")
    txt_email_confirm = (By.XPATH, "//table[@id='email_table']//tr[contains(@class, 'mail')]//td[contains(.,'Please confirm your account')]//span")
    txt_link_confirm = (By.XPATH, "//*[@id='display_email']//a[contains(@href,'Confirm')]")
    btn_mail = (By.XPATH, "//*[@id='inbox-id']")
    txt_mail_name = (By.XPATH, "//*[@id='inbox-id']/input")
    btn_set = (By.XPATH, "//*[@id='inbox-id']/button[@class='save button small']")
    slt_domain_name = (By.XPATH, "//select[@id='gm-host-select']")
    txt_email_reset = (By.XPATH, "//table[@id='email_table']//tr[contains(@class, 'mail')]//td[contains(.,'Please reset your password')]//span")
    txt_link_reset = (By.XPATH, "//*[@id='display_email']//a[contains(@href,'PasswordReset')]")
class SetHomepageLocator:
    msg_welcome = (By.XPATH, "//div[@id='content']/h1[text()='Welcome to Safe Railway']")
    msg_welcome_user = (By.XPATH, "//div[@id='banner']/div[@class='account']/strong")
    lnk_create_account = (By.XPATH, "//div[@id='content']//a[contains(@href,'Register')]")

class SetLoginPageLocator:
    txt_username = (By.ID, "username")
    txt_password = (By.ID, "password")
    btn_login = (By.XPATH, "//input[@type='submit']")
    msg_error = (By.XPATH, "//*[@id='content']/p[@class='message error LoginForm']")
    lnk_forgot_password = (By.XPATH, "//*[@id='content']//a[contains(@href,'ForgotPassword')]")
    txt_new_password = (By.ID, "newPassword")
    txt_confirm_password = (By.ID, "confirmPassword")
    txt_password_reset_token = (By.ID, "resetToken")
    btn_reset_password = (By.XPATH, "//form//input[@type='submit']")
    msg_reset = (By.XPATH, "//*[@id='content']/p[contains(@class,'message')]")
    msg_confirm_password = (By.XPATH, "//*[@id='content']//label[@class='validation-error' and @for='confirmPassword']")

class SetRegisterLocator:
    lbl_validation_error = "//*[@id='RegisterForm']//label[@for='%s' and @class='validation-error']"
    txt_email = (By.ID, "email")
    txt_password = (By.ID, "password")
    txt_confirm_password = (By.ID, "confirmPassword")
    txt_pid = (By.ID, "pid")
    btn_register = (By.XPATH, "//*[@id='RegisterForm']//p/input[@type='submit']")
    msg_error = (By.XPATH, "//*[@id='content']/p[@class='message error']")
    msg_success = (By.XPATH, "//*[@id='content']/h1[@align='center']")
    msg_confirm_success = (By.XPATH, "//*[@id='content']/p")

class SetForgotPasswordPage:
    txt_email = (By.ID, "email")
    btn_send = (By.XPATH, "//input[@value='Send Instructions']")