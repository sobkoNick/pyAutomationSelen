from reportportal_client import step
from selene import have
from selene.support import by
from selene.support.shared.jquery_style import s


class HomePage:
    def __init__(self):
        self.signed_in_alert = s(by.css('[class="common-flash-info"]'))
        self.user_menu_btn = s(by.css('[id="user-menu-button"]'))
        self.sign_out_btn = s(by.css('input[value="Sign Out"]'))

    @step
    def signed_in_alert_has_text(self, expected_text):
        return self.signed_in_alert.should(have.text(expected_text))

    @step
    def click_on_user_menu(self):
        self.user_menu_btn.click()
        return self

    @step
    def click_to_sign_out(self):
        self.sign_out_btn.click()
        return self

    @step
    def open_project(self, project):
        s(by.css(f'[title="{project}"]')).click()
        return self
