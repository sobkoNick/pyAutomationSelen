from _pytest.fixtures import fixture

import utils.config_util
from pages.home_page import HomePage
from pages.login_page import LoginPage


@fixture(scope="module")
def credentials():
    return utils.config_util.get_config("username"), utils.config_util.get_config("password")


def test_login_functionality(app, credentials):
    """
    Test performs login and verifies 'Signed in successfully' message is present
    """
    LoginPage() \
        .open_login_page() \
        .fill_email(credentials[0]) \
        .fill_password(credentials[1]) \
        .press_sign_in()
    HomePage().signed_in_alert_has_text('Signed in successfully')
