import json
from api_collections._base_api import BaseApi
from allure import step


class PostApi(BaseApi):
    def __init__(self, base_url='https://dummyapi.io/data/v1'):
        super().__init__(base_url)
        self.__url = '/post'
        self.__url_create = '/post/create'
        self.__headers = {
            'Content-Type': 'application/json',
            'app-id': '651d7e6ee9547b347e53b118'
        }

    @step
    def get_all_posts(self):
        return self._get(url=self.__url, headers=self.__headers)

    @step
    def create_new_post(self, user_data: dict):
        return self._post(self.__url_create, data=json.dumps(user_data), headers=self.__headers)

    @step
    def get_post_by_id(self, post_id: str):
        return self._get(url=f'{self.__url}/{post_id}', headers=self.__headers)

    @step
    def update_post_by_id(self, post_id: str, post_data: dict):
        return self._put(url=f'{self.__url}/{post_id}', headers=self.__headers, data=json.dumps(post_data))

    @step
    def delete_post_by_id(self, post_id: str):
        return self._delete(url=f'{self.__url}/{post_id}', headers=self.__headers)
