# 제출 버튼 클릭 시 "완료 메세지" + "다시 가입하기" 버튼 생성

import streamlit as st
import requests

def show_form():
    st.title('User Data Submission')
    with st.form("user_form"):
        user_id = st.text_input("ID")
        user_email = st.text_input("Email")
        user_name = st.text_input("Name")
        submitted = st.form_submit_button("Submit")

        if submitted:
            response = requests.post('https://us-central1-cloudfucntiontest-a21f8.cloudfunctions.net/add_userdb', json={
                'id': user_id,
                'email': user_email,
                'name': user_name
            })
            if response.ok:
                st.session_state['submitted'] = True
                st.rerun()  # 스크립트 재실행
            else:
                st.error("An error occurred.")

def show_success():
    st.markdown("<h1 style='text-align: center;'>회원 가입이 완료 되었습니다</h1>", unsafe_allow_html=True)
    if st.button("다시 가입하기"):
        st.session_state['submitted'] = False
        st.rerun()  # 스크립트 재실행

if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

if st.session_state['submitted']:
    show_success()
else:
    show_form()
