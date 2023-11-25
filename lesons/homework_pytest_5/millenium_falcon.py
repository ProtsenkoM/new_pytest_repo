import requests
import json
from requests.exceptions import RequestException

URL = 'https://swapi.dev/api/starships/'


class StarShip:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def create_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.__dict__, json_file, indent=4)


def get_pilot_info(pilots_url):
    pilots_info = []
    for pilots_ulr in starship['pilots']:
        pilot_response = requests.get(pilots_ulr)
        pilots_data = pilot_response.json()
        homeworld_response = requests.get(pilots_data['homeworld'])
        homeworld_data = homeworld_response.json()
        pilots_info.append({
            'name': pilots_data['name'],
            'height': pilots_data['height'],
            'mass': pilots_data['mass'],
            'homeworld': {
                'name': homeworld_data['name'],
                'url': homeworld_data['url'],
            }
        })
    return pilots_info


if __name__ == '__main__':
    try:
        response = requests.request('GET', url=URL, params={'search': 'Millennium Falcon'})
        assert response.status_code == 200
        data = response.json()
        starship = data['results'][0]
        pilots_url = starship['pilots']
        pilots_info = get_pilot_info(pilots_url)
        result_data = {
            'name': starship['name'],
            'max_speed': starship['max_atmosphering_speed'],
            'starship_class': starship['starship_class'],
            'pilots': pilots_info
        }

        millennium = StarShip(**result_data)
        millennium.create_json('starship.json')

    except RequestException as request_err:
        print(f'Request error {request_err}')
    except Exception as err:
        print(f'Some error {err}')
