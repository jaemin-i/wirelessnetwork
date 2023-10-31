from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import requests

url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'

queryParams = '?' + urlencode({quote_plus('serviceKey') : 'swQs7b7oxuStqf4FDNFpAOiwj3gTAk7cUtP76CWLv5pxHiQUkgkD6nkiHQXT8kN5DHZWcsaoa1PEzWsjvm+beQ=='
	, quote_plus('returnType') : 'xml'
	, quote_plus('numOfRows') : '10'
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
	print(datatime.get_text())
	print(pm25value.get_text())
