from wsgiref.simple_server import make_server
from cgi import parse_qs
import json

def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0
    response_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(response_body)

    sentence = d.get('sentence', [''][0])[0]
    character = d.get('character', [''][0])[0]

    length = len(sentence)
    re_count = sentence.count(character)

    status = '200 OK'
    response_body = json.dumps({'length':length, 'count':re_count})
	
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]
    
    start_response(status, response_headers)

    return [response_body]


