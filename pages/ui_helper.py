from selene.support import by
from selene.support.shared.jquery_style import s, ss


def by_id(value):
    return s(by.id(value))


def by_x(path):
    return s(by.xpath(path))


def by_css(path):
    return s(by.css(path))


def bys_x(path):
    return ss(by.xpath(path))


def bys_css(path):
    return ss(by.css(path))
