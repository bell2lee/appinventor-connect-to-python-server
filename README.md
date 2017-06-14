# appinventor-connect-to-python-server
파이썬 버전 2
# response value example
{"count": 4, "length": 26}
# send parameter test
curl -d 'sentence=This is a sample sentence.&character=s' http://localhost:8051
# 파일 설명
plain_server.py : 파이썬 웹 서버 기본 형식
remark_plain_server.py : 주석 추가

json_server.py : json 값을 리턴하는 웹 서버
remark_server.py : 주석 추가

count.py : wsgi 용 json_server.py
count.conf : /etc/apache2/conf-enabled 에 추가
# wsgi 설치
sudo apt-get install libapache2-mod-wsgi

