import json

import pytest
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
    LoginPage() \
        .open_login_page() \
        .fill_email(utils.config_util.get_config("username")) \
        .fill_password(utils.config_util.get_config("password")) \
        .press_sign_in()


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

@pytest.mark.skip(reason="No way to save test requirements and test steps")
def test_adding_test_case_to_suite(app, existing_suite):
    """
    Test adds a new test to existing suite and verifies data was saved correctly
    """
    HomePage().open_project(app.project_name)
    ProjectPage() \
        .choose_suite(existing_suite) \
        .choose_file_suite_type() \
        .click_to_add_new_test()\
        .set_test_name("created by autotest")\
        .set_test_requirements("req1")\
        .set_test_steps("step1")\
        .save_test()
