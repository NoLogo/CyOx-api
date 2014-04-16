import httplib


def get_route(*args):
    apikey = '8cc3ae75cfebd6aa'
    conn = httplib.HTTPConnection('www.cyclestreets.net')
    conn.request('GET', '/api/journey.json?key=' + apikey + '&plan=fastest&itinerarypoints=' + args[0] + '|' + args[1])
    response = conn.getresponse()
    conn.close()
    return response
