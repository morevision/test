import requests
import json

API_KEY = "504d665262686a693435624a574445"

# 전체 성공 여부 저장 변수
success = True  # 처음엔 모든 호출이 성공한다고 가정

# 2015년~2024년 반복
for year in range(2015, 2025):
    for month in range(1, 13):
        MONTH = f"{month:02d}"

        # URL 형식 고정
        url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/energyUseDataSummaryInfo/1/5/{year}/{MONTH}"

        # API 호출
        response = requests.get(url)

        # 실패 시 success 값을 False로 바꾸고 메시지 출력
        if response.status_code != 200:
            success = False
            print(f"❌ {year}년 {MONTH}월 데이터 호출 실패 (응답 코드: {response.status_code})")
            continue  # 다음 달로 넘어감

        # JSON 데이터 파싱 (출력은 생략)
        data = response.json()
        rows = data.get("energyUseDataSummaryInfo", {}).get("row", [])

        # 개인 유형 데이터만 처리 (출력하지 않음)
        for r in rows:
            if r.get("MM_TYPE") == "개인":
                pass  # 실제 데이터 출력 없이 그냥 넘어감

# 전체 결과 한 번만 출력
if success:
    print("\n전체 기간 API 호출 성공!")
else:
    print("\n일부 데이터 호출 실패가 발생했습니다.")
