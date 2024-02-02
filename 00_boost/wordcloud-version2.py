import streamlit as st
import streamlit_wordcloud as wordcloud

st.title('인터랙티브 워드클라우드 생성기')

# 예시 단어 목록
words = [
    {"text": "Python", "value": 100},
    {"text": "Data", "value": 80},
    {"text": "Streamlit", "value": 50},
    # 더 많은 단어를 추가할 수 있습니다
]

wc = wordcloud.visualize(words, tooltip_data_fields={
    'text':'Word', 'value':'Frequency'
}, per_word_coloring=False)

st.write(wc)
