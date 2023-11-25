import json

import pytest
from faker import Faker
from constants import ROOT_PATH
from page_objects.login_page import LoginPage
from utilities.driver_factory import DriverFactory
from utilities.json_to_dict import DictToClass


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='dev', help='Choose your env')
    parser.addoption('--hub', action='store', default='False', help='Run test in container Solenoid')
    parser.addoption('--headless', action='store', default='False', help='Run test in container Solenoid')


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test smoke"
    )
    config.addinivalue_line(
        "markers", "sanity: mark test sanity"
    )


@pytest.fixture(scope='session')
def env():
    with open(f'{ROOT_PATH}/configs/conf.json') as f:
        conf_dict = json.loads(f.read())
        return DictToClass(**conf_dict)


@pytest.fixture()
def create_driver(env, request):
    driver = DriverFactory(browser_id=env.browser_id,
                           hub=eval(request.config.getoption('--hub')),
                           headless=eval(request.config.getoption('--headless'))
                           ).get_driver()
    driver.maximize_window()
    driver.get(env.url)
    yield driver
    driver.quit()


@pytest.fixture
def get_user(env):
    return env.login, env.password


@pytest.fixture()
def login_to_bbc_without_user(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def login_to_bbc_with_user(create_driver, get_user):
    return LoginPage(create_driver).do_login(*get_user)


@pytest.fixture()
def login_and_open_news_page(create_driver, get_user):
    login_page = LoginPage(create_driver).do_login(*get_user)
    url = "https://www.bbc.com/news"
    news_page = login_page.open_news_page(url)
    return news_page


@pytest.fixture()
def login_and_open_sounds_page(create_driver, get_user):
    login_page = LoginPage(create_driver).do_login(*get_user)
    url = "https://www.bbc.co.uk/sounds"
    sounds_page = login_page.open_sounds_page(url)
    return sounds_page


@pytest.fixture()
def login_and_open_weather_page(create_driver, get_user):
    login_page = LoginPage(create_driver).do_login(*get_user)
    url = "https://www.bbc.com/weather"
    weather_page = login_page.open_weather_page(url)
    return weather_page


@pytest.fixture()
def fake():
    fake = Faker()
    return fake
