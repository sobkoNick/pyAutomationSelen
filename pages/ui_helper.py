from selene.core.entity import Element, Collection
from selene.core.query import text
from selene.support import by
from selene.support.shared.jquery_style import s, ss


def by_id(value) -> Element:
    return s(by.id(value))


def by_x(path) -> Element:
    return s(by.xpath(path))


def by_css(path) -> Element:
    return s(by.css(path))


def bys_x(path) -> Collection:
    return ss(by.xpath(path))


def bys_css(path) -> Collection:
    return ss(by.css(path))


def get_text(element: Element):
    element.get(query=text)
