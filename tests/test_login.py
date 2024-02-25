from _pytest.fixtures import fixture

import utils.config_util
from pages.login_page import LoginPage


@fixture(scope="module")
def credentials():
    return (utils.config_util.get_config("username"), utils.config_util.get_config("password"))


def test_login_functionality(app, credentials):
    # TODO Consider adding additional layer to have assertion there
    LoginPage() \
        .open_login_page() \
        .fill_email(credentials[0]) \
        .fill_password(credentials[1]) \
        .press_sign_in() \
        .signed_in_alert_has_text('Signed in successfully')
