from googlemaps import GoogleMaps


api_key = 'AIzaSyCaC09zWi98K5wSNy3YkJkoPNbS9YbZnL0'
gmaps = GoogleMaps(api_key)


def create_route(start_point, end_point):
    startpoint = gmaps.geocode(start_point)
    endpoint = gmaps.geocode(end_point)
    points = (startpoint, endpoint,)
    return points
