from wsgiref.simple_server import make_server
from cgi import parse_qs
import json

def application(environ, start_response):
    # 전달 받은 값의 사이즈 구하기
	try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0
	# 전달 받은 값을 넣기
    response_body = environ['wsgi.input'].read(request_body_size)
    # 분류해버리기
	d = parse_qs(response_body)
	
	# 분류한거 가져와서 변수에 저장하기
    sentence = d.get('sentence', [''][0])[0]
    character = d.get('character', [''][0])[0]

	# 과제 값 구하기
    length = len(sentence)
    re_count = sentence.count(character)

    status = '200 OK'
	# json형식으로 변환
    response_body = json.dumps({'length':length, 'count':re_count})
	
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]
    
    start_response(status, response_headers)
	
	# 저장한 값 리턴하기
    return [response_body]

httpd = make_server('localhost', 8051, application)
httpd.handle_request()

