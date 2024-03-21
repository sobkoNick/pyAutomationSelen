from reportportal_client import step
from selene.support import by
from selene.support.conditions import have
from selene.support.shared.jquery_style import s


class ProjectPage:
    def __init__(self):
        self.first_suite_input = s(by.css('input[placeholder="First Suite"]'))
        self.add_suite_btn = s(by.xpath('//button[text()="Suite"]'))
        self.suite_item = '//p[@class="nestedItem-title"]//span[text()="{suite_name}"]'
        self.opened_suite_title = s(by.css('[class="detailed-view-suite-body"] h3'))
        # Test fragment locators
        # todo create a fragment for this?
        self.add_new_test_btn = s(by.xpath('//a[contains(@href, "/new-test")]'))
        self.test_name_input = s(by.css('[placeholder="Title"]'))
        self.save_test_btn = s(by.xpath('//div[@class="detail-view-actions"]//button'))
        self.requirements_input = s(by.xpath('//*[@class="view-line"][2]'))
        self.steps_input = s(by.xpath('//*[@class="view-line"][4]'))

    @step
    def set_suite_name(self, name):
        self.first_suite_input.set(name)
        return self

    @step
    def click_to_add_suite(self):
        self.add_suite_btn.click()
        return self

    @step
    def choose_suite(self, suite_name):
        s(by.xpath(self.suite_item.format(suite_name=suite_name))).click()
        return self

    @step
    def verify_opened_suite_title(self, suite_title):
        self.opened_suite_title.should(have.exact_text(suite_title))
        return self

    @step
    def click_to_add_new_test(self):
        self.add_new_test_btn.click()
        return self

    @step
    def set_test_name(self, name):
        self.test_name_input.set(name)
        return self

    @step
    def set_test_requirements(self, requirements_text):
        # todo maybe it should set values from requirements_text like it's a list.
        self.requirements_input.set(requirements_text)
        return self

    @step
    def set_test_steps(self, steps_text):
        # todo and here also. check while testing
        self.steps_input.set(steps_text)
        return self

    @step
    def save_test(self):
        self.save_test_btn.click()
        return self
