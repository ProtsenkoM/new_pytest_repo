from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from page_objects.main_page import MainPage
from allure import step


class LoginPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_username_input = (By.XPATH, '//*[@id="user-identifier-input"]')
    __loc_password_input = (By.XPATH, '//*[@id="password-input"]')
    __loc_login_btn = (By.XPATH, '//*[@id="submit-button"]')
    __loc_reset_password = (By.XPATH, '//p[@class="button__label"]/a/span')
    __loc_link_to_forgot_password = (By.XPATH, "//span[contains(text(), 've forgotten my password')]")
    __loc_user_input_for_reset = (By.ID, 'user-identifier-input')
    __loc_check_inbox_message = (By.XPATH, "//span[contains(text(),'Please check your inbox')]")
    __loc_register_btn = (By.XPATH, "//span[contains(text(),'Register now')]")
    __loc_16_btn = (By.XPATH, '//div[@class="sb-flex-container"]/a[2]/span')
    __loc_day_input = (By.ID, 'day-input')
    __loc_month_input = (By.ID, 'month-input')
    __loc_year_input = (By.ID, 'year-input')
    __loc_user_identifier = (By.ID, "user-identifier-input")
    __loc_password_identifier = (By.ID, "password-input")
    __loc_registered_message = (By.XPATH, "//span[contains(text(),'re registered')]")

    @step
    def set_login(self, login: str):
        self._page.send_keys(self.__loc_username_input, login)
        return self

    @step
    def set_password(self, password: str):
        self._page.send_keys(self.__loc_password_input, password)
        return self

    @step
    def click_login_btn(self):
        self._page.click(self.__loc_login_btn)
        return MainPage(self._page.driver)

    @step
    def do_login(self, login, password):
        self.set_login(login)
        self.click_login_btn()
        self.set_password(password)
        return self.click_login_btn()

    @step
    def reset_pass(self):
        self._page.click(self.__loc_reset_password)
        self._page.click(self.__loc_link_to_forgot_password)
        return self

    @step
    def set_email_for_reset_pass(self, email: str):
        self._page.send_keys(self.__loc_user_input_for_reset, email)
        self._page.click(self.__loc_login_btn)
        return self

    @step
    def check_inbox_message(self):
        return self._page.is_displayed(self.__loc_check_inbox_message)

    @step
    def click_register_btn(self):
        self._page.click(self.__loc_register_btn)
        return self

    @step
    def click_16_or_over_btn(self):
        self._page.click_by_js(self.__loc_16_btn)
        return self

    @step
    def set_of_day(self, day: int):
        self._page.send_keys(self.__loc_day_input, day)

    @step
    def set_of_month(self, month: int):
        self._page.send_keys(self.__loc_month_input, month)

    def set_of_year(self, year: int):
        self._page.send_keys(self.__loc_year_input, year)

    @step
    def set_of_birth(self, day, month, year):
        self.set_of_day(day)
        self.set_of_month(month)
        self.set_of_year(year)
        self._page.click_by_js(self.__loc_login_btn)

    @step
    def set_of_email(self, email: str):
        self._page.send_keys(self.__loc_user_identifier, email)

    @step
    def set_of_password(self, password: str):
        self._page.send_keys(self.__loc_password_identifier, password)

    @step
    def registration(self, email, password):
        self.set_of_email(email)
        self.set_password(password)
        self._page.click_by_js(self.__loc_login_btn)

    @step
    def check_registration(self):
        return self._page.is_displayed(self.__loc_registered_message)
