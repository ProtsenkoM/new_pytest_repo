from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_is_visible(self, locator: tuple, timeout=5) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_element_is_clickable(self, locator: tuple, timeout=5) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_element_is_presence(self, locator: tuple, timeout=10) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def send_keys(self, locator: tuple, value):
        el = self.wait_element_is_visible(locator)
        el.send_keys(value)

    def click(self, locator: tuple):
        el = self.wait_element_is_clickable(locator)
        el.click()

    def click_by_return(self, locator: tuple):
        el = self.wait_element_is_clickable(locator)
        el.send_keys(Keys.RETURN)

    def is_displayed(self, locator: tuple):
        el = self.wait_element_is_visible(locator)
        return el.is_displayed()

    def click_by_js(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].click()', el)

    def get_elements_count(self, locator: tuple):
        self.wait_element_is_presence(locator)
        el = self.driver.find_elements(*locator)
        return len(el)

    def get_text(self, locator: tuple):
        self.wait_element_is_visible(locator)
        el = self.driver.find_element(*locator)
        return el.text

    def open_page(self, url: str):
        return self.driver.get(url)

    def scroll_into_view(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        self.driver.execute_script('arguments[0].scrollIntoView()', el)

    def scroll_to_element(self, locator: tuple):
        el = self.wait_element_is_presence(locator)
        ActionChains(self.driver).scroll_to_element(el).perform()

    def save_screenshot(self):
        self.driver.get_screenshot_as_file('screen.png')

    def local_storage_set_item(self, key, value):
        self.driver.execute_script(f'window.localStorage.setItem({key}, {value})')
