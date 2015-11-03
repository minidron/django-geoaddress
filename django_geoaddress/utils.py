# --coding: utf8--
import requests


def find(key, obj):
    """
    Поиск значения по ключу.
    """
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


def fetch_address(query):
    """
    Получить адрес с Яндекса.
    """
    url = u'http://geocode-maps.yandex.ru/1.x/?geocode=%s&format=json' % (
        query)

    try:
        r = requests.get(url).json()
    except requests.exceptions.RequestException:
        return None

    address = {}
    address['country'] = find('CountryName', r)
    address['area'] = find('AdministrativeAreaName', r)
    address['subarea'] = find('SubAdministrativeAreaName', r)
    address['locality'] = find('LocalityName', r)
    address['street'] = find('ThoroughfareName', r)
    address['house'] = find('PremiseNumber', r)

    address = {k: v for k, v in address.items() if v is not None}

    return address
