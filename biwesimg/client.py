import requests
import simplejson as json
import methods

class TimeoutError(requests.exceptions.Timeout): pass
class ConnectionError(Exception): pass

def is_success(r): return r.status_code in [200, 201]

FROM_URL = dict(headers={'X-Bws-File-Origin': 'url'})
FROM_FILE = dict(headers={'X-Bws-File-Origin': 'upload'})
JPEG = ('jpeg', )

class Client(object):
    API_URL = "http://biwes.com/app/imgconverter"
    __slots__ = ['api_key', 'secret', 'base_url', ]

    def __init__(self, base_url=API_URL, **kwargs):
        self.base_url = base_url
        for k in kwargs: setattr(self, k, kwrags[v])

    def make_request(self, method, data=None,
                     params=None, files=None,
                     headers={}):
        path, func = method
        the_headers = {'Content-Type': 'application/json'}
        the_headers.update(headers)
        try:
            return parse_response(func(
                self.base_url + path,
                params=None,
                timeout=7,
                files=files,
                headers=the_headers,
                data=json.dumps(params)
            ))
        except requests.exceptions.Timeout:
            raise TimeoutError()
        except:
            raise

    def image(self, **kwargs):
        return Image(_client=self, **kwargs)

class Response(object):
    __slots__ = ['http', 'success', 'result']
    def __init__(self, **kwargs):
        for k in kwargs: setattr(self, k, kwargs[k])

class Image(object):
    __slots__ = ['_response', '_client', 'size',
                 'from_url', 'url', 'from_file']
    def __init__(self, **kwargs):
        for k in kwargs: setattr(self, k, kwargs[k])

    def convert_to(self, image_format=JPEG, size=(1, 1)):
        try:
            headers = {}
            ext, = image_format
            if not self.from_url is None:
                headers.update(FROM_URL['headers'])
                r = self._client.make_request(
                    methods.CONVERT,
                    headers=headers,
                    params={
                        'url': self.from_url,
                        'format': ext,
                        'size': "%d %d" % size,
                    }
                )
                if r.success:
                    return Image(_client=self._client,
                        url=r.result.get('url', None),
                        size=tuple(r.result.get('size', ''))
                    )
                    self.url = r.result.get('url', None)
                return True

        except TimeoutError:
            return False
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
    url = "http://en.support.files.wordpress.com/2009/03/docurl1.png?w=599"
    c = Client(base_url="http://biwes.dev/app/imgconv")
    image = c.image(from_url=url)
    oimage = image.convert_to(JPEG, size=(256, 0))
    print oimage.size

