from _pytest.fixtures import fixture
from reportportal_client import step

import utils.config_util
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.project_page import ProjectPage


@step("Log in")
@fixture(autouse=True)
def perform_login(app):
    LoginPage() \
        .open_login_page() \
        .fill_email(utils.config_util.get_config("username")) \
        .fill_password(utils.config_util.get_config("password")) \
        .press_sign_in()


# todo add fixture to yield suite_name and then delete it with api call


def test_suite_creation(app, perform_login):
    HomePage().open_project("project1")  # todo get this from properties file
    suite_name = "first_test"
    ProjectPage() \
        .set_suite_name(suite_name) \
        .click_to_add_suite() \
        .choose_suite(suite_name) \
        .verify_opened_suite_title(suite_name)
