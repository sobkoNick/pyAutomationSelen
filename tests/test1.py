from pages.login_page import LoginPage


def test_try():
    LoginPage() \
        .open_login_page() \
        .fill_email("1") \
        .fill_password("2") \
        .press_sign_in()
