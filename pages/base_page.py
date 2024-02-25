from selene import by
from selene.core.entity import Element, Collection
from selene.core.query import text
from selene.support.shared.jquery_style import ss, s


class BasePage:
    def by_id(self, value) -> Element:
        return s(by.id(value))

    def by_x(self, path) -> Element:
        return s(by.xpath(path))

    def by_css(self, path) -> Element:
        return s(by.css(path))

    def bys_x(self, path) -> Collection:
        return ss(by.xpath(path))

    def bys_css(self, path) -> Collection:
        return ss(by.css(path))

    def get_text(self, element: Element):
        return element.get(query=text)
