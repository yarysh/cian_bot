import os

import requests


class Distance:
    @staticmethod
    def calc(origin):
        result = {'text': None, 'value': None}
        origin += ', Москва, Россия'
        resp = requests.get(
            'https://maps.googleapis.com/maps/api/distancematrix/json',
            params={
                'origins': origin,
                'destinations': '55.792589, 37.527588',
                'mode': 'walking',
                'language': 'ru',
                'key': os.getenv('GOOGLE_DISTANCE_API_KEY'),
            }
        )
        if resp.status_code != 200: return result

        data = resp.json()
        for route in data['rows']:
            for elem in route['elements']:
                if elem['status'] == 'OK' and elem['duration']['value']:
                    if not result['value'] or elem['duration']['value'] < result['value']:
                        result['value'] = elem['duration']['value']
                        result['text'] = elem['duration']['text']
        return result
