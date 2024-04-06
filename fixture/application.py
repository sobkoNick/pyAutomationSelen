from models.common_test_data import CommonTestData


class Application:
    def __init__(self):
        self.logger = None
        self.env = ""
        self.test_data: CommonTestData = None
