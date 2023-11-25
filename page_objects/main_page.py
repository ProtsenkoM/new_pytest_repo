from selenium.webdriver.common.by import By
from page_objects._base_page import BasePage
from page_objects.news_page import NewsPage
from page_objects.sounds_page import SoundsPage
from page_objects.weather_page import WeatherPage
from allure import step


class MainPage:
    def __init__(self, driver):
        self._page = BasePage(driver)

    __loc_logo = (By.XPATH, "//div[contains(text(), 'Welcome to the BBC')]")
    __loc_your_account = (By.XPATH, "//span[contains(text(), 'For you')]")
    __loc_logout = (By.XPATH, "//span[contains(text(), 'Sign out')]")
    __loc_logout_message = (By.XPATH, "//h1[contains(text(),'ve signed out, sorry to see you go')]")
    __loc_error_message = (By.XPATH, "//span[contains(text(),'That password')]")
    __loc_search_btn = (By.XPATH, "//span[contains(text(), 'Search')]")
    __loc_search_input = (By.XPATH, '//*[@id="searchInput"]')
    __loc_search_btn_on_page = (By.XPATH, '//*[@id="searchButton"]')
    __loc_search_result = (By.XPATH, '//*[@id="main-content"]/div[4]/div/div/ul/li[1]/div/div/div[1]/div[1]/a')
    __loc_count_topic = (By.XPATH,
                         '//*[@id="header-content"]/nav/div[1]/div/div[2]/ul[2]/li')  # Узято абслютний шлях для того щоб обійти динамічні класи в html
    __loc_main_article = (By.XPATH, '//div[@type="article"]//span')
    __loc_first_article = (By.XPATH, '//*[@id="main-content"]//h1')
    __loc_list_of_news = (By.XPATH, '//*[@id="main-content"]/div[3]/div/div/ul/li')  # Узято абслютний шлях для того щоб обійти динамічні класи в html

    @step
    def is_logo_displayed(self):
        return self._page.is_displayed(self.__loc_logo)

    @step
    def click_open_your_account(self):
        self._page.click(self.__loc_your_account)
        return self

    @step
    def click_logout(self):
        self._page.click(self.__loc_logout)
        return MainPage(self._page.driver)

    @step
    def is_logout_message_displayed(self):
        return self._page.is_displayed(self.__loc_logout_message)

    @step
    def get_title(self):
        return self._page.driver.title

    @step
    def click_search_btn(self):
        self._page.click(self.__loc_search_btn)
        return self

    @step
    def set_search_query(self, search_query: str):
        self._page.send_keys(self.__loc_search_input, search_query)
        self._page.click(self.__loc_search_btn_on_page)
        return self

    @step
    def search_result(self):
        self._page.is_displayed(self.__loc_search_result)
        return self

    @step
    def open_main_article(self):
        self._page.click_by_js(self.__loc_main_article)
        return NewsPage(self._page.driver)

    @step
    def is_error_message_displayed(self):
        if self._page.is_displayed(self.__loc_error_message):
            raise ValueError('Incorrect login or password')
        else:
            raise ValueError('Login was successfully done with incorrect login or password')

    @step
    def do_logout(self):
        self.click_open_your_account()
        return self.click_logout()

    @step
    def section_get_count(self):
        return self._page.get_elements_count(self.__loc_count_topic)

    @step
    def get_topic_of_article(self):
        return self._page.get_text(self.__loc_first_article)

    @step
    def get_count_news(self):
        return self._page.get_elements_count(self.__loc_list_of_news)

    @step
    def open_news_page(self, url):
        self._page.open_page(url)
        return NewsPage(self._page.driver)

    @step
    def open_sounds_page(self, url):
        self._page.open_page(url)
        return SoundsPage(self._page.driver)

    @step
    def open_weather_page(self, url):
        self._page.open_page(url)
        return WeatherPage(self._page.driver)
