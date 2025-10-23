
















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




import requests

api_key = "504d665262686a693435624a574445"

year = 2023
month = 1

url = f"http://openapi.seoul.go.kr:8088/{api_key}/json/energyUseDataSummaryInfo/1/5/{year}/{month:02d}"

response = requests.get(url)

if response.status_code == 200:
    print("API 호출 성공")
    print(response.json())
else:
    print(f" API 호출 실패: {response.status_code}")


