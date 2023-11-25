from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from allure import step


class SoundsPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_section_music = (By.XPATH, "//span[contains(text(), 'Music')]")
    __loc_trending_podcasts = (By.XPATH, '//*[@id="unmissable_speech"]//ul/li')
    __loc_podcasts = (By.XPATH, '//*[@id="unmissable_speech"]/div[2]/ul/li[1]/div/a')
    __loc_name_podcast = (By.XPATH, '//*[@class="sc-c-module-title gel-1/1"]/h2')
    __loc_episode = (By.XPATH, '//ul[@class="sc-c-list__items"]/li[1]//span')
    __loc_subscribe_btn = (By.XPATH, '//button[@data-bbc-content-label="subscribe"]')
    __loc_check_subscribed = (By.XPATH, "//div[contains(text(),'Subscribed')]")



    @step
    def get_title(self):
        return self._page.driver.title

    @step
    def open_section_music(self):
        self._page.click_by_js(self.__loc_section_music)

    @step
    def get_count_podcasts(self):
        return self._page.get_elements_count(self.__loc_trending_podcasts)

    @step
    def open_podcast_music(self):
        self._page.click_by_js(self.__loc_podcasts)
        return self

    @step
    def get_name_of_podcast(self):
        return self._page.get_text(self.__loc_name_podcast)

    @step
    def open_episode_in_podcast(self):
        self._page.click_by_js(self.__loc_episode)
        return self

    @step
    def click_subscribe_btn(self):
        self._page.click_by_js(self.__loc_subscribe_btn)
        return self

    @step
    def check_subscription(self):
        return self._page.get_text(self.__loc_check_subscribed)

    @step
    def click_detailed_btn(self):
        self._page.click_by_js(self.__loc_subscribe_btn)
        return self
