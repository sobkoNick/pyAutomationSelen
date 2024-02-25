from copy import copy

import pytest
from reportportal_client import step
from selene import browser
from selenium import webdriver

import settings
import utils.config_util
from fixture.application import Application
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

    set_up_browser()

    return fixture


@step("Set up browser")
def set_up_browser():
    browser.config.base_url = utils.config_util.get_config('base_url')

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_experimental_option("detach", True)
    browser.config.driver = webdriver.Chrome(options=options)
