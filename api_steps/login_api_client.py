import curl
import requests
from reportportal_client import step
from requests import Response

from api_steps.api_client import ApiClient
from utils.config_util import get_config


class LoginApiClient(ApiClient):
    def __init__(self, endpoint, logger):
        super().__init__(endpoint=endpoint, logger=logger)

    @step
    def get_jwt(self) -> Response:
        api_token_key = "api_token"
        token = get_config(api_token_key)

        response = requests.post(url=self.post_url, params=[(api_token_key, token)])
        self.logger.info(f"Request \n{curl.parse(response, print_it=False, return_it=True)}")
        self.logger.info(f"Response \ncode = {response.status_code}\ntext = {response.text}")

        self.response = response
        return response

    def send_jwt_request(self):
        self.get_jwt()
        return self
