import pystreamapi
from _pytest.fixtures import fixture

import utils.config_util
from api_steps.api_client import ApiClient
from constants.endpoint_names import SUITES_ENDPOINT
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.project_page import ProjectPage


@fixture(autouse=True)
def perform_login(app):
    """
    Test precondition to perform login
    """
    LoginPage() \
        .open_login_page() \
        .fill_email(utils.config_util.get_config("username")) \
        .fill_password(utils.config_util.get_config("password")) \
        .press_sign_in()


@fixture
def suite_name(app):
    name = "selene_autotest_suite_1"

    yield name

    app.logger.info('Deleting the created suite using API')
    all_suites = ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
        .get([app.project_id]) \
        .validate_that() \
        .status_code_is_ok() \
        .get_response_body()

    found_suite = pystreamapi.Stream.of(all_suites['data']) \
        .filter(lambda suite: suite['attributes']['title'] == name) \
        .find_first()

    if found_suite.is_present():
        ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
            .delete([app.project_id, found_suite.get()['id']]) \
            .validate_that() \
            .status_code_is_ok()


def test_suite_creation(app, suite_name, perform_login):
    HomePage().open_project(app.project_name)
    ProjectPage() \
        .set_suite_name(suite_name) \
        .click_to_add_suite() \
        .choose_suite(suite_name) \
        .verify_opened_suite_title(suite_name)
