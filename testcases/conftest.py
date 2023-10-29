import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import get_property

web_driver = None



@pytest.fixture(scope='class')
def init_driver(request, browser):
    global web_driver
    if browser == "chrome":
        options = Options()
        options.add_argument('--ignore-ssl-errors=yes')

        options.add_argument('--ignore-certificate-errors')
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser == "headless":
        # ser = Service("./Drivers/chromedriver.exe")
        options = Options()
        options.headless = True
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        service = Service(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service, options=options)
        # web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser == "firefox":
        ser = Service(executable_path="Path of Browser")
        web_driver = webdriver.Firefox(service=ser)
    else:
        options = Options()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    request.cls.driver = web_driver
    web_driver.get(str(get_property("url")))
    web_driver.implicitly_wait(15)
    web_driver.maximize_window()
    yield
    web_driver.quit()


@pytest.fixture(scope='class')
def browser(request):
    return request.config.getoption('--browser')


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Run browser in headless mode")


# @pytest.fixture
# def allure_setup(request):
#     from allure_commons.types import AttachmentType
#     from allure import attachment
#
#     yield
#
#     # Add Allure attachments for screenshots, logs, etc.
#     attachment(name="Screenshot", body=request.node.screenshot, attachment_type=AttachmentType.PNG)
#


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        # extra.append(pytest_html.extras.url("http://www.example.com/"))
        # report.extra = extra
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='test_failed_screenshot',
                attachment_type=allure.attachment_type.PNG)
