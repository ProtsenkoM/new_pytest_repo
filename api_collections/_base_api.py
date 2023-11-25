import requests


class BaseApi:
    def __init__(self, base_url):
        self.__base_url = base_url
        self.__headers = {}
        self.__requests = requests

    def _get(self, url, headers=None):
        if not headers:
            headers = self.__headers
        response = self.__requests.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def _post(self, url, data, headers=None):
        if not headers:
            headers = self.__headers
        response = self.__requests.post(f'{self.__base_url}{url}', data=data, headers=headers)
        return response

    def _path(self):
        pass

    def _delete(self, url, headers=None):
        if not headers:
            headers = self.__headers
        response = self.__requests.delete(f'{self.__base_url}{url}', headers=headers)
        return response

    def _put(self, url, data,  headers=None):
        if not headers:
            headers = self.__headers
        response = self.__requests.put(f'{self.__base_url}{url}', data=data,  headers=headers)
        return response
