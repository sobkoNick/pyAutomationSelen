from dataclasses import dataclass, field


# todo use pydantic
@dataclass(init=False, repr=True, eq=True)
class TestAttributes:
    title: str
    suite_id: str = field(default=None)
    # the value is not present when we get all suites.
    description: str = field(default="")


@dataclass(init=False, repr=True, eq=True)
class Test:
    type: str
    attributes: TestAttributes
    id: str = field(default=None)

    # need to add this otherwise user_credentials will be a dict
    def __post_init__(self):
        self.attributes = TestAttributes(**self.attributes)
