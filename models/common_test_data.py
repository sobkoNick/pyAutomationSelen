from dataclasses import dataclass


@dataclass(frozen=True)
class Credentials:
    username: str
    password: str


@dataclass
class CommonTestData:
    jwt_token: str
    # next fields are loaded from the qa_config.json file
    project_id: str
    project_name: str
    base_url: str
    login_url: str
    user_credentials: Credentials

    # need to add this otherwise user_credentials will be a dict
    def __post_init__(self):
        self.user_credentials = Credentials(**self.user_credentials)
