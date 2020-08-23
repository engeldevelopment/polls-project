from behave import fixture, use_fixture
from selenium.webdriver import Firefox


@fixture
def browser_firefox(context):
    context.browser = Firefox()
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(browser_firefox, context)
