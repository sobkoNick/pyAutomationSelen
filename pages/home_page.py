from reportportal_client import step
from selene import have

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.signed_in_alert = self.by_css('[class="common-flash-info"]')

    @step
    def signed_in_alert_has_text(self, expected_text):
        return self.signed_in_alert.should(have.text(expected_text))
