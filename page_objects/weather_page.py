from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from allure import step


class WeatherPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_input_city = (By.XPATH, '//*[@id="ls-c-search__input-label"]')
    __loc_button_search = (By.XPATH, '//button[@title="Search for a location"]')
    __loc_city_name = (By.XPATH, '//h1[@id="wr-location-name-id"]')
    __loc_button_detailed_map = (By.XPATH, "//span[contains(text(),'Detailed map')]")
    __loc_city_name_on_map = (By.XPATH, "//div[contains(text(),'Kyiv')]")
    __loc_list_of_features = (By.XPATH, "//div[contains(@id, 'simple-promo-collection')]/div/div/div/ul/li")
    __loc_city_on_globe = (By.XPATH, "//span[contains(text(),'Chicago')]")

    @step
    def get_title(self):
        return self._page.driver.title

    @step
    def set_city(self, city: str):
        self._page.send_keys(self.__loc_input_city, city)
        return self

    @step
    def click_return(self):
        self._page.click_by_return(self.__loc_button_search)
        return self

    @step
    def get_city_name(self):
        return self._page.get_text(self.__loc_city_name)

    @step
    def click_detailed_btn(self):
        self._page.click_by_js(self.__loc_button_detailed_map)
        return self

    @step
    def get_city_name_on_map(self):
        return self._page.get_text(self.__loc_city_name_on_map)

    @step
    def get_count_features(self):
        return self._page.get_elements_count(self.__loc_list_of_features)

    @step
    def click_city_on_globe_btn(self):
        self._page.click_by_js(self.__loc_city_on_globe)
        return self



