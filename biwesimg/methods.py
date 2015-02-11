from requests import post, get, put, patch, delete


MAKE_CHANNEL = ('/channel', post, )
DELETE_CHANNEL = ('/channel', delete, )
SEND_MESSAGE = ('/channel', None, )