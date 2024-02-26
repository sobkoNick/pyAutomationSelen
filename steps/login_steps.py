from pages.login_page import LoginPage
from steps.home_steps import HomeSteps


class LoginSteps:
    def login_with_credentials(self, username, password) -> HomeSteps:
        LoginPage() \
            .open_login_page() \
            .fill_email(username) \
            .fill_password(password) \
            .press_sign_in()
        return HomeSteps()
