import json
from api_collections._base_api import BaseApi
from allure import step


class UserApi(BaseApi):
    def __init__(self, base_url='https://dummyapi.io/data/v1'):
        super().__init__(base_url)
        self.__url = '/user'
        self.__url_create = '/user/create'
        self.__headers = {
            'Content-Type': 'application/json',
            'app-id': '651d7e6ee9547b347e53b118'
        }

    @step('Get full list of users')
    def get_all_users(self):
        return self._get(url=self.__url, headers=self.__headers)

    @step
    def get_user_by_id(self, user_id: str):
        return self._get(url=f'{self.__url}/{user_id}', headers=self.__headers)

    @step
    def update_user_by_id(self, user_id: str, user_data: dict):
        return self._put(url=f'{self.__url}/{user_id}', headers=self.__headers, data=json.dumps(user_data))

    @step
    def post_new_user(self, user_data: dict):
        return self._post(self.__url_create, data=json.dumps(user_data), headers=self.__headers)

    @step
    def delete_user_by_id(self, user_id: str):
        return self._delete(url=f'{self.__url}/{user_id}', headers=self.__headers)
