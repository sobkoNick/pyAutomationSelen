import json

from assertpy import assert_that
from reportportal_client import step
from requests import Response


class Validator:
    def __init__(self, response: Response):
        self.response = response

    @step
    def status_code_is_ok(self):
        actual_status_code = self.response.status_code
        assert_that(actual_status_code, f"Actual status code {actual_status_code} is not 200 OK") \
            .is_equal_to(200)
        return self

    @step
    def status_code_is(self, status_code):
        actual_status_code = self.response.status_code
        assert_that(actual_status_code,
                    f"Actual status code {actual_status_code} differs from expected {status_code}") \
            .is_equal_to(status_code)
        return self

    @step
    def body_contains(self, expected_obj):
        """
        Verifies response body with list of items contains expected_obj
        :param expected_obj: class must have static method 'build' to build actual response obj
        """
        actual_objs = []
        for obj in self.get_response_body()['data']:
            # here I get class from expected_obj and call its method build()
            actual_objs.append(expected_obj.__class__.build(json.dumps(obj)))
        assert_that(actual_objs, f"Response \n{actual_objs} \n does not contain expected \n{expected_obj}\n") \
            .is_not_empty().contains(expected_obj)
        return self

    @step
    def body_equals(self, expected_obj):
        """
        Verifies response body equals expected_obj
        :param expected_obj: class must have static method 'build' to build actual response obj
        """
        # here I get class from expected_obj and call its method build()
        actual_obj = expected_obj.__class__.build(json.dumps(self.get_response_body()['data']))
        assert_that(actual_obj, f"Response \n{actual_obj} \n does not equal expected \n{expected_obj}\n") \
            .is_equal_to(expected_obj)
        return self

    def get_response_body(self):
        return self.response.json()
