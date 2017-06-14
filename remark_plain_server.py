from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = [ # 반환할 내용
		# environ으로 넘어온 각종 서버, 파이썬 등 정보등을 순차적으로 넣음
        '%s: %s' %(key, value) for key, value in sorted(environ.items())
    ]
	
    response_body = '\n'.join(response_body) # 배열로 생성 된 내용을 엔터로 구분지어 스트링으로 변환

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body))) # 페이지 길이 지정
    ]

    start_response(status, response_headers)

    return [response_body] # 바디 내용 반환

httpd = make_server('localhost', 8051, application)
httpd.handle_request()
