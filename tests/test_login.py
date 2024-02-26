from _pytest.fixtures import fixture

import utils.config_util
from pages.login_page import LoginPage
from steps.login_steps import LoginSteps


@fixture(scope="module")
def credentials():
    return (utils.config_util.get_config("username"), utils.config_util.get_config("password"))


def test_login_functionality(app, credentials):
    # TODO what approach to use? with steps or directly using page object methods?
    LoginSteps().login_with_credentials(credentials[0], credentials[1]) \
        .verify_login_message('Signed in successfully')

    # LoginPage() \
    #     .open_login_page() \
    #     .fill_email(credentials[0]) \
    #     .fill_password(credentials[1]) \
    #     .press_sign_in() \
    #     .signed_in_alert_has_text('Signed in successfully')
