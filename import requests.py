# --------------------------------------------------------------------------
# 1. 데이터 수집 및 전처리 (기존 코드)
# --------------------------------------------------------------------------
import requests
import pandas as pd

API_KEY = "504d665262686a693435624a574445"
personal_data = []

for year in range(2015, 2025):
    for month in range(1, 13):
        MONTH = f"{month:02d}"
        url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/energyUseDataSummaryInfo/1/5/{year}/{MONTH}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            rows = data.get("energyUseDataSummaryInfo", {}).get("row", [])
            for r in rows:
                if r.get("MM_TYPE") == "개인":
                    personal_data.append(r)

df = pd.DataFrame(personal_data)
df["월"] = df["MON"].astype(int)
df["year"] = df["YEAR"].astype(int)

def get_season(month):
    if 3 <= month <= 5: return "봄"
    elif 6 <= month <= 8: return "여름"
    elif 9 <= month <= 11: return "가을"
    else: return "겨울"

df["season"] = df["월"].apply(get_season)

# --------------------------------------------------------------------------
# 2. 시각화를 위한 데이터 가공
# --------------------------------------------------------------------------
# matplotlib 라이브러리를 가져옵니다.
import matplotlib.pyplot as plt
import platform

# 한글 폰트 설정 (Windows, Mac, Linux/Colab 자동 지원)
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    plt.rc('font', family='AppleGothic')
else: # Linux or Colab
    plt.rc('font', family='NanumGothic')

# 그래프의 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 에너지 사용량 컬럼들을 숫자형으로 변환 (문자/None 값은 0으로 처리)
energy_cols = ['EUS', 'GUS', 'WUS', 'HUS']
for col in energy_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# 총 사용량 컬럼 생성 (전기+가스+수도+지역난방)
df['total_usage'] = df[energy_cols].sum(axis=1)

# 연도별로 총 사용량의 합계를 계산
yearly_total_usage = df.groupby('year')['total_usage'].sum()

# --------------------------------------------------------------------------
# 3. 선 그래프 시각화 및 저장
# --------------------------------------------------------------------------
# 그래프 크기 설정
plt.figure(figsize=(12, 6))

# 선 그래프 그리기
plt.plot(yearly_total_usage.index, yearly_total_usage.values, marker='o', linestyle='-')

# 그래프 제목 설정 
student_id_suffix = "8458" # 학번
plt.title(f'연도별 에너지 총 사용량 변화 - {student_id_suffix}')

# X축, Y축 라벨 설정
plt.xlabel('연도')
plt.ylabel('총 에너지 사용량 (단위: 사용량 합계)')

# 그리드 추가
plt.grid(True, linestyle='--', alpha=0.6)

# 그래프 파일로 저장
file_name = f"연도별_에너지_사용량_변화_{student_id_suffix}.png"
plt.savefig(file_name)

# 그래프 화면에 표시
plt.show()

print(f"\n그래프가 '{file_name}'으로 저장되었습니다.")