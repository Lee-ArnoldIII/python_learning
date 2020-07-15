import requests

class InvalidValueError(Exception):
    pass

def api_lookup(url):
    assert isinstance(url, str)

    if not url.startswith('http'):
        raise InvalidValueError('The URL to look up from is not valid.')

    return requests.get(url).content


print(api_lookup('http://www.google.com'))


print(list(map(lambda z: z**2, [x for x in range(10)])))