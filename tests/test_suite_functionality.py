import json

import pystreamapi
from _pytest.fixtures import fixture

import utils.config_util
from api_steps.api_client import ApiClient
from constants.endpoint_names import SUITES_ENDPOINT
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.project_page import ProjectPage


#   ---FIXTURES---

@fixture(autouse=True)
def perform_login(app):
    """
    Test precondition to perform login
    """
    LoginPage().login(utils.config_util.get_config("username"), utils.config_util.get_config("password"))


suites = ['selene_autotest_suite_1', 'selene_autotest_suite_2']


# Something like data provider. suites -> request.
# 'suites' are used as parameter, but each list item is passed in request.param
@fixture(params=suites)
def suite_name(app, request):
    name = request.param
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


@fixture
def existing_suite(app):
    with open("tests/test_data/existing_suite.json") as json_data:
        data = json.load(json_data)

    # creates default suite for tests
    suite = ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
        .post(url_params=[app.project_id], new_obj=data) \
        .validate_that().status_code_is_ok().get_response_body()
    # suite = Suite.build(json.dumps(suite['data']))

    # passes suite name
    yield suite['data']['attributes']['title']

    app.logger.info("Deleting existing suite after test run")
    ApiClient(token=app.token, endpoint=SUITES_ENDPOINT, logger=app.logger) \
        .delete(url_params=[app.project_id, suite['data']['id']]).validate_that()


#   ---TESTS---

def test_suite_creation(app, suite_name):
    """
    Test creates a new suite, opens it and verifies the name in a title field
    """
    HomePage().open_project(app.project_name)
    ProjectPage() \
        .set_suite_name(suite_name) \
        .click_to_add_suite() \
        .choose_suite(suite_name) \
        .verify_opened_suite_title(suite_name)


def test_suite_is_present_on_ui(app, existing_suite):
    """
    Test opens existing suite (created using API) and verifies the name in a title field
    """
    HomePage().open_project(app.project_name)
    ProjectPage() \
        .choose_suite(existing_suite) \
        .verify_opened_suite_title(existing_suite)
