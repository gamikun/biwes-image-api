import requests
import simplejson as json

class TimeoutError(requests.exceptions.Timeout): pass
class ConnectionError(Exception): pass

def is_success(r): return r.status_code in [200, 201]

class Client(object):
    API_URL = "http://biwes.com/app/imgconverter"
    __slots__ = ['api_key', 'secret', 'base_url',]

    def __init__(self, base_url=API_URL, **kwargs):
        self.base_url = base_url
        for k in kwargs: setattr(self, k, kwrags[v])

    def make_request(self, method, data=None, params=None):
        path, func = method
        try:
            return parse_response(func(
                self.base_url + path,
                params=params,
                timeout=7,
            ))
        except requests.exceptions.Timeout:
            raise TimeoutError()
        except:
            raise

    def __call__(self, name, **kwargs):
        if name == 'channel':
            return Channel(_client=self, **kargs)

class Response(object):
    __slots__ = ['http', 'success', 'result']
    def __init__(self, **kwargs):
        for k in kwargs: setattr(self, k, kwargs[k])

class Channel(object):
    __slots__ = ['_client', 'id']
    def __init__(self, **kwargs):
        for k in kwargs: setattr(self, k, kwargs[k])

    def create(self):
        try:
            
        except TimeoutError:
            return False

def parse_response(response):
    return Response(
        http=response,
        result=parse_response_content(response),
        success=is_success(response)
    )

def parse_json(content):
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return None

def parse_response_content(response):
    ctype = response.headers.get('content-type', '')
    if ctype.startswith('application/json'):
        return parse_json(response.content)

if __name__ == "__main__":
    from methods import MAKE_CHANNEL
    r = Client(base_url="http://biwes.dev/app/imgconv")
    response = r.make_request(MAKE_CHANNEL)
    print response.result
    print response.http.status_code
