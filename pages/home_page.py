from reportportal_client import step
from selene import have
from selene.support import by
from selene.support.shared.jquery_style import s


class HomePage:
    def __init__(self):
        self.signed_in_alert = s(by.css('[class="common-flash-info"]'))

    @step
    def signed_in_alert_has_text(self, expected_text):
        return self.signed_in_alert.should(have.text(expected_text))
