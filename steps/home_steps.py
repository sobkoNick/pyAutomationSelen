from assertpy import assert_that

from pages.home_page import HomePage


class HomeSteps:
    def __init__(self):
        self.home_page = HomePage()

    def verify_login_message(self, expected_message):
        actual_text = self.home_page.get_signed_in_alert_text()
        assert_that(actual_text, f"Actual alert text {actual_text} differs from expected {expected_message}") \
            .is_equal_to(expected_message)
