import pytest

from api_collections.data_classes.user_dataclass import UserData
from api_collections.post_api import PostApi
from api_collections.user_api import UserApi


@pytest.fixture()
def get_fake_user_payload(fake):
    return {
        "firstName": fake.name(),
        "lastName": fake.last_name(),
        "email": fake.email()
    }


@pytest.fixture()
def get_new_user_id(get_fake_user_payload):
    response = UserApi().post_new_user(user_data=get_fake_user_payload)
    data = response.json()
    return data['id']


@pytest.fixture()
def get_mock_user_by_id():
    def __inner(user_id):
        resp = UserApi().get_user_by_id(user_id=user_id)  # like data from DB
        return UserData(**resp.json())
    return __inner


@pytest.fixture()
def get_fake_post_payload(fake, get_new_user_id):
    return {
        "text": fake.sentence(10),
        "image": "https://randomuser.me/api/portraits/women/58.jpg",
        "likes": 100,
        "tags": "qa",
        "owner": get_new_user_id
    }


@pytest.fixture()
def get_new_post_id(get_fake_post_payload):
    response = PostApi().create_new_post(user_data=get_fake_post_payload)
    data = response.json()
    return data['id']


@pytest.fixture()
def get_mock_post_by_id():
    def __inner(post_id):
        resp = PostApi().get_post_by_id(post_id=post_id)  # like data from DB
        return UserData(**resp.json())
    return __inner

