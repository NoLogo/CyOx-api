import requests


API_KEY = '8cc3ae75cfebd6aa'
API_URL = 'http://www.cyclestreets.net/api/journey.json'


def flip_coords(coords):
    return ','.join(reversed(coords.split(',')))


def make_coord_obj(coord_string):
    longitude, latitude = coord_string.split(',')
    return {
        'longitude': longitude,
        'latitude': latitude,
    }


def get_route(start, end):
    start = flip_coords(start)
    end = flip_coords(end)
    api_args = {
        'key': API_KEY,
        'plan': 'fastest',
        'itinerarypoints': '|'.join([start, end]),
    }
    response = requests.get(API_URL, params=api_args)
    data = response.json()
    if data:
        finaldata = []
        for point in data['marker']:
            point_attrs = point['@attributes']
            points = point_attrs.get('points')
            if points:
                point_attrs['points'] = map(make_coord_obj, points.split(' '))
            finaldata.append(point_attrs)
        return {
            'summary': finaldata[0],
            'waypoints': finaldata[1:],
        }
    return {}
