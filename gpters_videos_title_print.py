import requests
from bs4 import BeautifulSoup
import re

# 크롤링할 페이지의 URL
url = 'https://www.youtube.com/@gpters/videos'

# URL에서 페이지 내용을 가져옵니다.
response = requests.get(url)

# 페이지 내용을 BeautifulSoup으로 파싱합니다.
soup = BeautifulSoup(response.text, 'html.parser')

# HTML 문자열을 문자열로 변환
html_string = str(soup)

# start_string와 end_string 사이의 텍스트를 정규 표현식을 사용하여 추출합니다.
start_string = '}]},"title":{"runs":[{"text":"'
end_string = '"}]'

pattern = re.compile(re.escape(start_string) + '(.*?)' + re.escape(end_string), re.DOTALL)
matches = re.findall(pattern, html_string)

# 찾은 텍스트를 하나씩 출력합니다.
for i_count, match in enumerate(matches):
    print(i_count+1, match)
