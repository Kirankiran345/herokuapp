from pages.login_page import Loginpage
from testcases.test_base import BaseTest
from utils import get_property


class TestLogin(BaseTest):

    def __init__(self, driver):
        self.lp = Loginpage(driver)

    def test_home_page(self):
        title = self.lp.get_page_title()
        assert title == "Contact List App"

    def test_login_page(self):
        self.lp.enter_username(get_property("username"))
        self.lp.enter_password(get_property("password"))
        self.lp.click_submit_button()
