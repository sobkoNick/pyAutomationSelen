from copy import copy

import pytest
from reportportal_client import step
from selene import browser
from selenium import webdriver

import settings
import utils.config_util
from api_steps.login_api_client import LoginApiClient
from constants import endpoint_names
from fixture.application import Application
from pages.home_page import HomePage
from pages.project_page import ProjectPage
from utils import config_util
from utils.logger import CustomLogger


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="dev or qa"
    )


@pytest.fixture(scope="session")
def app(request):
    global fixture
    fixture = Application()
    fixture.logger = CustomLogger().set_up(__name__)

    fixture.env = request.config.getoption("--env")
    settings.ENV = copy(fixture.env)

    fixture.token = request_and_verify_jwt(fixture.logger)
    fixture.project_id = config_util.get_config("project_id")
    fixture.project_name = config_util.get_config("project_name")

    set_up_browser()

    yield fixture

    browser.quit()


@pytest.fixture(autouse=True)
def logout_after_test():
    yield
    project_page = ProjectPage()
    if project_page.is_account_btn_visible():
        project_page.click_on_account_btn()
    HomePage().click_on_user_menu().click_to_sign_out()
    browser.driver.delete_all_cookies()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attaches a screenshot on Report Portal on test failure
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        fixture.logger.error(f"{rep.head_line} {rep.outcome}",
                             attachment={"name": f"{rep.head_line}.png",
                                         "data": browser.config.driver.get_screenshot_as_png(),
                                         "mime": "image/png"})


@step("Set up browser")
def set_up_browser():
    browser.config.base_url = utils.config_util.get_config('base_url')

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_experimental_option("detach", True)
    browser.config.driver = webdriver.Chrome(options=options)


@step("Sends request from fixture to get jwt token")
def request_and_verify_jwt(logger):
    jwt_response = LoginApiClient(endpoint_names.LOGIN_ENDPOINT, logger).get_jwt()
    code = jwt_response.status_code
    jwt_token = jwt_response.json()["jwt"]
    if code != 200 or not jwt_token.strip():
        pytest.skip(f"Unable to get JWT token. Status code - {code}, token - {jwt_token}")
    return jwt_token
