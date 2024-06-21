import requests
import pandas as pd
from datetime import datetime

# 상수 정의
API_KEY = 'api_key'
API_URL = 'https://apis.data.go.kr/1230000/BidPublicInfoService04/getBidPblancListInfoServc01'
RESPONSE_FORMAT = 'json'

# 사용자 입력 받기
numOfRows = input("한 페이지 결과 수: ")
pageNo = input("페이지 번호: ")
inqryDiv = input("조회 구분 (1:등록일시, 2:입찰공고번호, 3:변경일시): ")
inqryBgnDt = input("조회 시작 일시 (yyyymmddhhmm): ")
inqryEndDt = input("조회 종료 일시 (yyyymmddhhmm): ")
bidNtceNo = input("입찰공고번호 (선택 사항, 없으면 빈칸으로 두세요): ")

# API 호출 파라미터 설정
params = {
    'serviceKey': API_KEY,
    'numOfRows': numOfRows,
    'pageNo': pageNo,
    'inqryDiv': inqryDiv,
    'inqryBgnDt': inqryBgnDt,
    'inqryEndDt': inqryEndDt,
    'type': RESPONSE_FORMAT
}

if bidNtceNo:
    params['bidNtceNo'] = bidNtceNo

# API 호출
response = requests.get(API_URL, params=params)
data = response.json()

# 결과를 DataFrame으로 변환
df = pd.DataFrame(data['response']['body']['items']['item'])

# 파일 이름 생성 및 CSV 파일로 저장
filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{inqryBgnDt}_{inqryEndDt}_{pageNo}.csv"
df.to_csv(filename, index=False)

print(f"파일 '{filename}'에 저장되었습니다.")
