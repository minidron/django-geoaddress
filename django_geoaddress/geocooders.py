#--coding: utf8--

import ast
import requests


YANDEX = {
    'url': 'http://geocode-maps.yandex.ru/1.x/?',
    'query_name': 'geocode',
    'params': {
        'format': 'json',
    },
}


def find(key, obj):
    if key in obj:
        return obj[key]
    elif isinstance(obj, dict):
        for k in obj:
            result = find(key, obj[k])
            if result:
                return result
    elif isinstance(obj, list):
        for k in obj:
            result = find(key, k)
            if result:
                return result
    else:
        return None


def yandex(data):
    """
    Геокодер Яндекса.
    """
    query = u', '.join(data).replace(' ', '+')
    url = u'%s%s=%s' % (YANDEX['url'], YANDEX['query_name'], query)
    try:
        r = requests.get(url, params=YANDEX['params'])
        r.encoding = 'utf-8'
        coordinates = find('pos', ast.literal_eval(r.text))
        if coordinates:
            latitude, longitude = coordinates.split(' ')
            coordinates = {
                'latitude': latitude,
                'longitude': longitude,
            }
            return coordinates
    except requests.exceptions.RequestException:
        return None
    return None
