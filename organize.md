# streamlit

## 터미널 명렁어
- streamlit run 파일이름: 파일 실행.

## 기본형태
```python
import streamlit as st

def main(): # streamlit을 이용한 웹 표현 함수.
    st.title('웹 대시보드')

if __name__ == '__main__': # 이 파일에서 실행할 때만
    main() # 함수 실행.
```

## 출력 관련 함수
- st.title(값): 값을 제목(엄청 큰 텍스트)으로 해서 출력
- st.header(값): 값을 헤더(큰 텍스트)로 해서 출력
- st.subheader(값): 값을 서브헤더(조금 큰 텍스트)로 해서 출력
- st.text(값): 값을 텍스트로 해서 출력
- st.success('초록 텍스트창과 글씨')
- st.warning('노랑 텍스트창과 글씨')
- st.info('파랑 텍스트창과 글씨')
- st.error('빨강 텍스트창과 글씨')
- st.help(함수): 함수를 자동으로 설명해주는 텍스트창 생성.
- st.dataframe(df): 데이터프레임을 출력
- st.write(값): 값을 출력, 텍스트나 데이터프레임 등 다 가능.

## 조건문 넣기 좋은 함수
- st.button('버튼'): '버튼'이라는 버튼 생성 # boolean값 리턴.
- st.radio('설명할 텍스트', ['1번 항목', '2번 항목']): 설명할 텍스트와 함께 선택할 수 있는 여러 항목 생성. # 항목 이름 리턴.
- st.checkbox('네모박스'): 네모난 체크박스 생성. # boolean값 리턴.
- st.selectbox('설명할 텍스트', 이터러블값): 두번째 파라미터에 리스트 같은 것을 넣어서 이용자의 선택에 따라 이터러블값의 원소를 리턴.