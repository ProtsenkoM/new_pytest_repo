from http import HTTPStatus
from api_collections.data_classes.user_dataclass import UserData
from api_collections.post_api import PostApi
from api_collections.user_api import UserApi


def test_get_users():
    """
    Test get all users
    :rtype: object
    """
    response = UserApi().get_all_users()
    assert response.status_code == HTTPStatus.OK, f'Request fail({response.text})'
    data = response.json()
    assert isinstance(data, dict), f'Incorrect type of object come from response'


def test_create_user(get_fake_user_payload):
    """
    Testing creation of new user
    :rtype: object
    """
    payload = get_fake_user_payload
    response = UserApi().post_new_user(user_data=payload)
    assert response.status_code == HTTPStatus.OK, f'Request fail({response.text})'
    data = response.json()
    assert data['firstName'] == payload['firstName']


def test_get_user_by_id(get_new_user_id, get_mock_user_by_id):
    """
    Test getting user by id
    :rtype: object
    """
    _id = get_new_user_id
    response = UserApi().get_user_by_id(user_id=_id)
    assert response.status_code == HTTPStatus.OK, f'Request fail({response.text})'
    user_data = UserData(**response.json())
    actual_data_from_db = get_mock_user_by_id(_id)
    assert user_data.get_dict() == actual_data_from_db.get_dict(),  f'Different data between db and response'


def test_create_user_without_email():
    """
    Test creation of new user with incorrect parameters
    :rtype: object
    """
    payload = UserData.get_fake_user_payload()
    payload.pop('email')
    response = UserApi().post_new_user(user_data=payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST, f'Request fail({response.text})'


def test_update_user_by_id(get_new_user_id, get_mock_user_by_id):
    """
    Test update of already created users with different parameters
    :rtype: object
    """
    _id = get_new_user_id
    response = UserApi().update_user_by_id(user_id=_id, user_data=UserData.get_fake_user_without_email())
    assert response.status_code == HTTPStatus.OK, f'Request fail({response.text})'
    user_data = UserData(**response.json())
    actual_data_from_db = get_mock_user_by_id(_id)
    assert user_data.get_dict() == actual_data_from_db.get_dict(),  f'Different data between db and response'


def test_delete_user_by_id(get_new_user_id):
    """
    Test deletion of already created users
    :rtype: object
    """
    _id = get_new_user_id
    response = UserApi().delete_user_by_id(user_id=_id)
    check_obj = UserApi().get_user_by_id(_id)
    assert check_obj.status_code == HTTPStatus.NOT_FOUND, f'Request fail({response.text})'


def test_get_posts():
    """
    Test get all post and check the type
    :rtype: object
    """
    response = PostApi().get_all_posts()
    assert response.status_code == HTTPStatus.OK, f'Request fail({response.text})'
    data = response.json().get('data')
    assert isinstance(data, list), f'Incorrect type of object come from response'


def test_create_post(get_fake_post_payload):
    """
    Test creation of new post
    :rtype: object
    """
    payload = get_fake_post_payload
    response = PostApi().create_new_post(user_data=payload)
    assert response.status_code == HTTPStatus.OK, f'Request fail({response.text})'
    data = response.json()
    assert data['owner']['id'] == payload['owner'],  f'Owner id has other id after creation'


def test_get_post_by_id(get_new_post_id, get_mock_post_by_id):
    """
    Test getting post by id
    :rtype: object
    """
    _id = get_new_post_id
    response = PostApi().get_post_by_id(post_id=_id)
    assert response.status_code == HTTPStatus.OK, f'Request fail({response.text})'
    user_data = UserData(**response.json())
    actual_data_from_db = get_mock_post_by_id(_id)
    assert user_data.get_dict() == actual_data_from_db.get_dict(), f'Different data between db and response'


def test_update_post_by_id(get_new_post_id, get_mock_post_by_id):
    """
    Test update already created post by other data
    :rtype: object
    """
    _id = get_new_post_id
    response = PostApi().update_post_by_id(post_id=_id, post_data=UserData.get_fake_post_payload())
    assert response.status_code == HTTPStatus.OK, f'Request fail({response.text})'
    user_data = UserData(**response.json())
    actual_data_from_db = get_mock_post_by_id(_id)
    assert user_data.get_dict() == actual_data_from_db.get_dict(), f'Different data between db and response'


def test_delete_post_by_id(get_new_post_id):
    """
    Test deletion of already created post
    :rtype: object
    """
    _id = get_new_post_id
    response = PostApi().delete_post_by_id(post_id=_id)
    check_obj = PostApi().get_post_by_id(_id)
    assert check_obj.status_code == HTTPStatus.NOT_FOUND, f'Request fail({response.text})'

