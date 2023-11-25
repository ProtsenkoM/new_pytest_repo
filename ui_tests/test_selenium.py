import pytest
import random
from page_objects.login_page import LoginPage


# 5 test cases for login page https://account.bbc.com/
@pytest.mark.smoke
def test_login(login_to_bbc_without_user, get_user):
    """
    Test login to https://account.bbc.com/ with correct credentials
    :param login_to_bbc_without_user:
    :param get_user:
    """
    main_page = login_to_bbc_without_user.do_login(*get_user)
    assert main_page.is_logo_displayed(), 'Login failed'


@pytest.mark.smoke
def test_login_bad_credentials(login_to_bbc_without_user):
    """
    Test login to https://account.bbc.com/ with fake credentials
    :param login_to_bbc_without_user:
    """
    credentials = ('mishunya4@gmail.com', 'M123456@')
    main_page = login_to_bbc_without_user.do_login(*credentials)
    with pytest.raises(ValueError, match='Incorrect login or password'):
        main_page.is_error_message_displayed()


@pytest.mark.smoke
def test_logout(login_to_bbc_with_user):
    """
    Test logout from https://account.bbc.com/
    :param login_to_bbc_with_user:
    """
    main_page = login_to_bbc_with_user.do_logout()
    assert main_page.is_logout_message_displayed(), 'logout failed'


@pytest.mark.smoke
def test_check_reset_pass(create_driver):
    """
    Test reset password for user
    :param create_driver:
    """
    pass_reset_page = LoginPage(create_driver)
    pass_reset_page.reset_pass().set_email_for_reset_pass('mail@mail.com')
    assert pass_reset_page.check_inbox_message(), 'Email was not sent'


@pytest.mark.smoke
def test_registration_new_user(create_driver, fake):
    """
    Test registration of new user on https://account.bbc.com/
    :param create_driver:
    :param fake:
    """
    fake_day = random.randint(1, 31)
    fake_month = random.randint(1, 12)
    fake_year = random.randint(1970, 2007)
    faker_login = fake.email()
    faker_pass = "M123456!"
    registration_page = LoginPage(create_driver)
    registration_page.click_register_btn().click_16_or_over_btn()
    registration_page.set_of_birth(fake_day, fake_month, fake_year)
    registration_page.registration(faker_login, faker_pass)
    assert registration_page.check_registration(), 'Registration was not completed'


# 5 test cases for Main page https://www.bbc.com/
@pytest.mark.sanity
def test_check_title_on_page(login_to_bbc_without_user, get_user):
    """
    Test check title after login to the system
    :param login_to_bbc_without_user:
    :param get_user:
    """
    main_page = login_to_bbc_without_user.do_login(*get_user)
    main_page_title = main_page.get_title()
    assert main_page_title == 'BBC - Home', 'logged to incorrect page'


@pytest.mark.sanity
def test_search_on_page(login_to_bbc_without_user, get_user):
    """
    Test of search for topic "Technology"
    :param login_to_bbc_without_user:
    :param get_user:
    """
    main_page = login_to_bbc_without_user.do_login(*get_user)
    assert main_page.click_search_btn().set_search_query("Technology").search_result(), 'There are no search result '


@pytest.mark.sanity
def test_check_topic_count(login_to_bbc_without_user, get_user):
    """
    Test check count of topics on main page
    :param login_to_bbc_without_user:
    :param get_user:
    """
    news_page = login_to_bbc_without_user.do_login(*get_user)
    exc_count = 8
    assert news_page.section_get_count() == exc_count, 'Oops! Wrong topic counter'


@pytest.mark.sanity
def test_open_first_article(login_to_bbc_without_user, get_user):
    """
    Test open of first article on main page
    :param login_to_bbc_without_user:
    :param get_user:
    """
    news_page = login_to_bbc_without_user.do_login(*get_user)
    news_page.open_main_article()
    page_title = news_page.get_title()
    new_topic = news_page.get_topic_of_article()
    assert page_title[:-11] == new_topic, 'Oops! Wrong article was opened'


@pytest.mark.sanity
def test_check_count_news_on_main_page(login_to_bbc_without_user, get_user):
    """
    Test count of news on main page.
    :param login_to_bbc_without_user:
    :param get_user:
    """
    news_page = login_to_bbc_without_user.do_login(*get_user)
    exc_count = 4
    count_news = news_page.get_count_news()
    assert count_news == exc_count, 'Oops! Wrong news counter'


# 5 test cases for Third page https://www.bbc.com/news
@pytest.mark.sanity
def test_open_news_page(login_and_open_news_page):
    """
    Test open NEWS page after login to BBC
    :param login_and_open_news_page:
    """
    news_page = login_and_open_news_page
    assert news_page.get_title() == "Home - BBC News", 'Oops! Wrong page opened'


@pytest.mark.sanity
def test_count_category_news_page(login_and_open_news_page):
    """
    Test count of sections of news on News page
    :param login_and_open_news_page:
    """
    news_page = login_and_open_news_page
    expected_count = 14
    news_page.get_count_sections()
    assert news_page.get_count_sections() == expected_count, 'Oops! Incorrect count of sections'


@pytest.mark.sanity
def test_open_category(login_and_open_news_page):
    """
    Open first category  of news
    :param login_and_open_news_page:
    """
    news_page = login_and_open_news_page
    news_page.click_section_btn()
    title = news_page.get_title()
    assert news_page.get_topic_of_section() == title[:-11]


@pytest.mark.sanity
def test_open_first_promo_news(login_and_open_news_page):
    """
    Open promo news on News page
    :param login_and_open_news_page:
    """
    news_page = login_and_open_news_page
    news_page.open_promo_news()
    title = news_page.get_title()
    text_promo_news = news_page.get_text_promo_news()
    assert text_promo_news == title.split(':', 1)[1].strip()[:-11], 'Oops promo news was not opened'


@pytest.mark.sanity
def test_get_count_most_watched_news(login_and_open_news_page):
    """
    Test count of watched news on News page
    :param login_and_open_news_page:
    """
    news_page = login_and_open_news_page
    assert news_page.get_count_most_watched_news() == 5, 'Oops, not all news were loaded'


# 5 test cases for Fourth page https://www.bbc.co.uk/sounds
@pytest.mark.sanity
def test_check_title_of_sound_page(login_and_open_sounds_page):
    """
    Test title on Sounds page
    :param login_and_open_sounds_page:
    """
    sound_page = login_and_open_sounds_page
    assert sound_page.get_title() == "BBC Sounds - Music. Radio. Podcasts", 'Oops sounds page was not opened'


@pytest.mark.sanity
def test_open_section_music(login_and_open_sounds_page):
    """
    Test open sections on Sounds page
    :param login_and_open_sounds_page:
    """
    sound_page = login_and_open_sounds_page
    sound_page.open_section_music()
    assert sound_page.get_title() == "BBC Sounds - Music", 'Oops section music was not opened'


@pytest.mark.sanity
def test_count_trending_podcast(login_and_open_sounds_page):
    """
    Test count of podcasts on Sounds page
    :param login_and_open_sounds_page:
    """
    sound_page = login_and_open_sounds_page
    sound_page.get_count_podcasts()
    assert sound_page.get_count_podcasts() == 6, 'Oops not all podcasts were loaded'


def test_open_podcast(login_and_open_sounds_page):
    """
    Test open of first podcast on Sounds page
    :param login_and_open_sounds_page:
    """
    sound_page = login_and_open_sounds_page
    sound_page.open_podcast_music()
    name_podcast = sound_page.get_name_of_podcast()
    title = sound_page.get_title()
    assert title.split('-')[1].strip() == name_podcast, 'Oops podcast was not loaded'


def test_subscription_on_episode(login_and_open_sounds_page):
    """
    Test subscription on Podcast
    :param login_and_open_sounds_page:
    """
    sound_page = login_and_open_sounds_page
    sound_page.open_podcast_music().open_episode_in_podcast().click_subscribe_btn()
    assert sound_page.check_subscription() == "Subscribed", 'Oops subscription was not done'


# 5 test cases for Fifth page https://www.bbc.com/weather
@pytest.mark.sanity
def test_title_of_weather_page(login_and_open_weather_page):
    """
    Test title on Weather page
    :param login_and_open_weather_page:
    """
    weather_page = login_and_open_weather_page
    assert weather_page.get_title() == "BBC Weather - Home", 'Oops weather page was not opened'


@pytest.mark.sanity
def test_weather_for_city(login_and_open_weather_page):
    """
    Test find weather for city
    :param login_and_open_weather_page:
    """
    weather_page = login_and_open_weather_page
    weather_page.set_city("London, Canada").click_return()
    assert weather_page.get_city_name() == "London", 'Oops London city was not opened'


@pytest.mark.sanity
def test_detailed_map(login_and_open_weather_page):
    """
    Test find city on Detailed map
    :param login_and_open_weather_page:
    """
    weather_page = login_and_open_weather_page
    weather_page.click_detailed_btn()
    assert weather_page.get_city_name_on_map() == "Kyiv", 'Oops Kyiv city on map was not found'


@pytest.mark.sanity
def test_count_of_features(login_and_open_weather_page):
    """
    Test count of features on Weather page
    :param login_and_open_weather_page:
    """
    weather_page = login_and_open_weather_page
    assert weather_page.get_count_features() == 5, 'Oops not all features on page was loaded'


@pytest.mark.sanity
def test_open_city_from_globe(login_and_open_weather_page):
    """
    Test open city from globe and check weather
    :param login_and_open_weather_page:
    """
    weather_page = login_and_open_weather_page
    weather_page.click_city_on_globe_btn()
    assert weather_page.get_city_name() == "Chicago", 'Oops Chicago city was not opened'
