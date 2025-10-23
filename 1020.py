import requests

url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty" 
api_key = "a3ERY4puvBY*********************************************************"

params = {
'serviceKey': api_key, 'returnType': 'json', 'numOfRows': '100',
'pageNo': '1',
'sidoName': '서울',
'ver': '1.0'
}
response = requests.get(url, params=params) if response.status_code == 200:
print("api 호출 성공") print(response.json())
else:
print(f"API 호출 실패: {response.status_code}")
