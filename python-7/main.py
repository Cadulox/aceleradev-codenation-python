import requests


def get_temperature(lat, lng):
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)
    try:
        reponse = requests.get(url)
        data = reponse.json()
        temperature = data.get('currently').get('temperature')
        if not temperature:
            return
        return int((temperature - 32) * 5.0 / 9.0)
    except requests.exceptions.RequestException as ex:
        return ex
    except AttributeError as ex:
        return ex
