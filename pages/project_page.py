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
