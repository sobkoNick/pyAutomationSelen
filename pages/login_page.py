from reportportal_client import step
from selene import browser

import utils.config_util
from pages.home_page import HomePage
from pages.ui_helper import *


class LoginPage:
    def __init__(self):
        self.email_input = by_css('#content-desktop #user_email')
        self.password_input = by_css('#content-desktop #user_password')
        self.sing_in_btn = by_css('#content-desktop [type="submit"]')

    @step
    def open_login_page(self):
        browser.open(utils.config_util.get_config('login_url'))
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
    def press_sign_in(self) -> HomePage:
        self.sing_in_btn.click()
        return HomePage()
