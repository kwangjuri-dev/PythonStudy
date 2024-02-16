import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Streamlit 페이지 설정
st.title('워드클라우드 생성기')

# 파일 업로드 섹션
uploaded_file = st.file_uploader("텍스트 파일을 업로드하세요", type="txt")
if uploaded_file is not None:
    # 파일 이름 확인
    file_name = uploaded_file.name

    # 파일 읽기
    text_data = uploaded_file.read().decode('utf-8')

    # 'KakaoTalk'이 파일명에 있을 경우 특정 단어 필터링
    if 'KakaoTalk' in file_name:
        filter_words = ["[나광웅]", "[정승아]", "[나은영]", "[나서영💗]", "사진", "이모티콘"]
        for word in filter_words:
            text_data = text_data.replace(word, "")

    # 한글 폰트 파일 경로 지정
    font_path = 'NanumGothic.ttf'  # 예: 'fonts/NanumGothic.ttf'

    # WordCloud 객체 생성
    wordcloud = WordCloud(font_path=font_path, width=800, height=400, background_color='white').generate(text_data)

    # 워드클라우드 그리기
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # Streamlit에 이미지 표시
    st.pyplot(plt)
