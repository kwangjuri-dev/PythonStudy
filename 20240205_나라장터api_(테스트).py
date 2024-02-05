import requests
import pandas as pd
from datetime import datetime

# 상수 정의
API_KEY = '%2FGWeXDVICEYiihLtJFWegEFmlNRZMdTIxn2xCOk3VlyjxHzF2jeL2gqLfzDDIJPkL5DxfmXbpA4wEDvL1QaQLQ%3D%3D'

BASE_URL = 'https://apis.data.go.kr/1230000/BidPublicInfoService04/getBidPblancListInfoServc01'

RESPONSE_FORMAT = 'json'

# 요청 헤더에 User-Agent 추가
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 사용자 입력 받기
# numOfRows = input("한 페이지 결과 수: ")
# pageNo = input("페이지 번호: ")
# inqryDiv = input("조회 구분 (1:등록일시, 2:입찰공고번호, 3:변경일시): ")
# inqryBgnDt = input("조회 시작 일시 (yyyymmddhhmm): ")
# inqryEndDt = input("조회 종료 일시 (yyyymmddhhmm): ")
# bidNtceNo = input("입찰공고번호 (선택 사항, 없으면 빈칸으로 두세요): ")

# (임시) 사용자 입력 일괄 받기.
numOfRows = '10'
pageNo = '1'
inqryDiv = '1'
inqryBgnDt = '202401020000'
inqryEndDt = '202401020930'
bidNtceNo = ''

# API URL 생성

api_url = f"{BASE_URL}?serviceKey={API_KEY}&numOfRows={numOfRows}&pageNo={pageNo}&inqryDiv={inqryDiv}&inqryBgnDt={inqryBgnDt}&inqryEndDt={inqryEndDt}&type={RESPONSE_FORMAT}"

if bidNtceNo:
    api_url += f"&bidNtceNo={bidNtceNo}"

print(api_url)

# API 호출
try:
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # 상태 코드가 400 또는 500대일 때 HTTPError 예외 발생
    data = response.json()

    # 결과를 DataFrame으로 변환
    df = pd.DataFrame(data['response']['body']['items'])

    # 파일 이름 생성 및 CSV 파일로 저장
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{inqryBgnDt}_{inqryEndDt}_{pageNo}.csv"
    df.to_csv(filename, index=False, encoding='utf-8-sig')

    print(f"파일 '{filename}'에 저장되었습니다.")

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)

