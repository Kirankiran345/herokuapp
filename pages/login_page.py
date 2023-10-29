from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class Loginpage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.driver.title

    def enter_username(self,text):
        self.driver.find_element(By.ID, "email").send_keys(text)

    def enter_password(self,text):
        self.driver.find_element(By.ID, "password").send_keys(text)

    def click_submit_button(self):
        self.driver.find_element(By.ID, "submit").submit()
