from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from allure import step


class NewsPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_list_sections = (By.XPATH, '//nav[@class="nw-c-nav__wide"]/ul/li')
    __loc_third_section = (By.XPATH, '//nav[@class="nw-c-nav__wide"]/ul/li[3]')
    __loc_name_of_third_section = (By.XPATH, '//nav[@class="nw-c-nav__wide"]/ul/li[3]/a/span[1]')
    __loc_promo_news = (By.XPATH, '//*[@id="news-top-stories-container"]//div[@class="gel-wrap"]/div/a/h3')
    __loc_title_promo_news = (By.XPATH, '//h1[@id="lx-event-title"]')
    __loc_count_most_watched_news = (By.XPATH, '//*[@class="gel-layout gel-layout--no-flex"]/li')

    @step
    def get_title(self):
        return self._page.driver.title

    @step
    def get_count_sections(self):
        return self._page.get_elements_count(self.__loc_list_sections)

    @step
    def click_section_btn(self):
        self._page.click(self.__loc_third_section)

    @step
    def get_topic_of_section(self):
        return self._page.get_text(self.__loc_name_of_third_section)

    @step
    def get_text_promo_news(self):
        return self._page.get_text(self.__loc_title_promo_news)

    @step
    def open_promo_news(self):
        self._page.click_by_js(self.__loc_promo_news)

    @step
    def get_count_most_watched_news(self):
        return self._page.get_elements_count(self.__loc_count_most_watched_news)
