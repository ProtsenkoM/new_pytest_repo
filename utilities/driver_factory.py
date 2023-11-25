from selenium.webdriver import Chrome, Firefox, ChromeOptions, FirefoxOptions
from selenium import webdriver

from constants import HUB_URL

_CHROME_ID = 1
_FIREFOX_ID = 2


class DriverFactory:
    def __init__(self, browser_id: int, hub=False, headless=False):
        self.__browser_id = browser_id
        self.__hub = hub
        self.__headless = headless
        self._selenoid_caps = {
            "enableVNC": True,
            "enableLog": True
        }

    def get_driver(self):
        if int(self.__browser_id) == _CHROME_ID:
            return self.__get_chrome_driver()
        elif int(self.__browser_id) == _FIREFOX_ID:
            return self.__get_firefox_driver()
        else:
            return self.__get_chrome_driver()

    def __get_chrome_driver(self):
        _options = ChromeOptions()
        _selenoid_caps = self._selenoid_caps.copy()
        if self.__headless:
            _selenoid_caps['enableVNC'] = False
            _options.add_argument('--headless')

        if self.__hub:
            _options.set_capability('selenoid:options', _selenoid_caps)
            #_options.browser_version = '117'
            driver = webdriver.Remote(
                command_executor=HUB_URL,
                options=_options)
            return driver
        else:
            _options.browser_version = '114'
            driver = Chrome(options=_options)
            return driver

    def __get_firefox_driver(self):
        _options = FirefoxOptions()
        _selenoid_caps = self._selenoid_caps.copy()
        if self.__headless:
            _selenoid_caps['enableVNC'] = False
            _options.add_argument('--headless')
        if self.__hub:
            _options.set_capability('selenoid:options', _selenoid_caps)
            driver = webdriver.Remote(
                command_executor=HUB_URL,
                options=_options)
            return driver
        else:
            driver = Firefox()
            return driver
