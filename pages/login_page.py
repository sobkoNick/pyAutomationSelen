from reportportal_client import step
from selene import browser
from selene.support import by
from selene.support.shared.jquery_style import s

import utils.config_util


class LoginPage:
    def __init__(self):
        self.email_input = s(by.css('#content-desktop #user_email'))
        self.password_input = s(by.css('#content-desktop #user_password'))
        self.sing_in_btn = s(by.css('#content-desktop [type="submit"]'))

    @step
    def login(self, login_url, credentials):
        self.open_login_page(login_url)
        self.fill_email(credentials.username)
        self.fill_password(credentials.password)
        self.press_sign_in()
        return self

    @step
    def open_login_page(self, login_url):
        browser.open(login_url)
        return self

    @step
    def fill_email(self, email):
        self.email_input.set(email)
        return self

    @step
    def fill_password(self, password):
        self.password_input.set(password)
        return self

    @step
    def press_sign_in(self):
        self.sing_in_btn.click()
        return self
