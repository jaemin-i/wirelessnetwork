from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import requests
import serial
import pyfirmata
import time

cmd = 'temp'

seri = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = None)
seri.write(cmd.encode())

url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'

queryParams = '?' + urlencode({quote_plus('serviceKey') : 'swQs7b7oxuStqf4FDNFpAOiwj3gTAk7cUtP76CWLv5pxHiQUkgkD6nkiHQXT8kN5DHZWcsaoa1PEzWsjvm+beQ=='
	, quote_plus('returnType') : 'xml'
	, quote_plus('numOfRows') : '1'
	, quote_plus('pageNo') : '1'
	, quote_plus('stationName') : '주안'
	, quote_plus('dataTerm') : 'DAILY'
	, quote_plus('ver') : '1.0'})
	
res = requests.get(url + queryParams)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find_all('item')

for item in data:
	datatime = item.find('datatime')
	pm25value = item.find('pm25value')
	
board = pyfirmata.Arduino('/dev/ttyACM0')

board.digital[7].mode = pyfirmata.OUTPUT
board.digital[6].mode = pyfirmata.OUTPUT
    
a = 1
while a:
	if seri.in_waiting != 0:
		content = seri.readline()
		print(f'시간 : {datatime.get_text()}')
		print(f'실외농도 : {pm25value.get_text()}')
		print(f'실내농도 : {content.decode()}')
		if(int(pm25value.get_text()) < float(content.decode())):
			print('창문을 열어 환기하세요')
			board.digital[7].write(1)
			board.digital[6].write(0)
		else:
			board.digital[7].write(0)
			board.digital[6].write(1)
		a = 0
		

