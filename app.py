# 가상환경 : 환경을 통일
# $conda create -n 가상환경이름 python=3.9 openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn
# conda는 아나콘다 명령어, create 가상환경 만들기, -n은 옵션, 파일이름, 설치할 파이썬, 파이썬에 맞는 라이브러리 등등
# '$conda create -n app_dash python=3.9 openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn'
# cycd -> 데브옵스


# conda activate base 들어가기
# conda deactivate base 나가는거


import streamlit as st

def main():
    st.title('앱 대시보드') # st는 화면 관련해서 처리
    st.text('데이터 분석 앱입니다.')
    st.text('텍스트 앱입니다.')

if __name__ == '__main__':
    main()

# $ streamlit run app.py
# 컨트롤c는 서버 끄는거
