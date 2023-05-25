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

## 선택 관련 함수
- st.button('버튼'): '버튼'이라는 버튼 생성 # boolean값 리턴.
- st.radio('설명할 텍스트', ['1번 항목', '2번 항목']): 설명할 텍스트와 함께 선택할 수 있는 여러 항목 생성. # 항목 이름 리턴.
- st.checkbox('네모박스'): 네모난 체크박스 생성. # boolean값 리턴.
- st.selectbox('설명할 텍스트', 이터러블값): 두번째 파라미터에 리스트 같은 것을 넣어서 이용자의 선택에 따라 이터러블값의 원소를 리턴.
- st.multiselect('설명할 텍스트', 이터러블값): 선택한 값들을 리스트로 리턴.
ex: 이터러블 값에 df.columns로 컬럼을 모은 리스트를 줘서 선택한 컬럼만 출력하도록 가능
- st.slider('설명문', min_value=x, max_value=y, step=z, value=a):  min부터 max까지의 숫자를 step간격으로 이동하며 값을 정함(기본값은 value).  함수의 기본값은 min은 0, max는 100, step은 1, 타입은 정수형으로 정의됨.  
- with st.expander(설명문):  
    st.text('안녕하세요.')  
    st.text('반값습니다.')  
: 설명문을 누를 경우 밑에 텍스트들이 표시.
### 사이드메뉴
- st.sidebar: 사이드바 생성.
ex:  
```python
menu = ['이미지 업로드', 'csv 업로드', 'About']
choice = st.sidebar.selectbox('메뉴', menu)
if choice == menu[0]:
    st.subheader('이미지 파일 업로드')
    run_app_image()
```

## 미디어 관련 함수
### from PIL import Image
- st.image(Image.open('경로'), use_columns_width=True): 경로에 있는 이미지를 화면을 꽉 채워서 보여줌. use_columns는 선택요소(괄호 안 함수는 변수에 따로 할당해서 넣어도 됨.)
- st.image('이미지 주소'): 인터넷에 이미지 주소를 그대로 가져와서 사용 가능.
- st.video(open('경로'), 'rb'): 경로에 있는 영상 출력
- st.file_uploader('설명문', type=확장자): 파일을 업로드.
확장자 ex: 이미지의 경우 ['png', 'jpg', 'jpeg'] 같이 묶어서 가능. import os를 통해 파일도 저장 가능.

## 인풋 관련
- st.text_input('설명문'): 텍스트를 친 뒤 엔터를 치면 해당 텍스트 리턴. max_chars=x을 붙이면 텍스트 최대길이 x, 'value='로 기본값 설정 가능.(eval() 함수를 활용해도 좋아보임.)
- st.number_input('설명문'): 숫자를 입력받아 리턴. 타입 기본값은 float이며, (설명문, 최솟값, 최댓값)을 설정 가능. 최솟값을 1과 같은 정수형을 넣을 경우 int형으로 바뀜.
- st.date_input('설명문'): 날짜를 입력받으며, 기본값은 현재날짜. 타입은 date타입.
- st.time_input('설명문'): 시간을 조정. 기본값은 15분씩 조정가능.
- st.text_input('설명문', type='password'): 비밀번호와 같이 OOOO으로 표시. 값이 보이지 않을 뿐이지 출력해보면 존재함.
- st.color_picker('설명문'): 색을 지정할 수 있음. 변수로 저장해서 st.text로 출력할 경우 헥스코드 출력.

## 데이터프레임 관련
- st.dataframe(df): df라는 데이터프레임 출력(st.write도 가능.)
- sp.pyplot(차트영역): 차트를 보여줌
- st.line_chart(df[컬럼]): 데이터프레임을 라인차트로 보여줌. () 안을 df[]가 담긴 리스트를 통해 여러개 한번에 시각화 가능
- st.area_chart(df[컬럼]): 영역차트로 보여줌
- st.bar_chart(df): 바차트로 보여줌
- st.map(df, x): 맵차트를 보여줌. x가 클수록 차트 확대.
### import altair as alt
- st.altair_chart(차트): 산점도 차트를 보여줌
ex:  
```python
chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species'
    ) # x와 y 설정 후 'species'를 기준으로 색을 나눔.
    st.altair_chart(chart) # 차트 출력
```
### import plotly.express as px
- 파이차트(비율을 볼 때):
ex:  
```python
fig = px.pie(df, 'lang', 'Sum', title='각 언어별 비율')
# df의 lang컬럼의 종류를 수치화한 sum을 통해 비율을 알아보기.
st.plotly_chart(fig) # 차트 출력
```
- 바차트
ex:  
```python
df = df.sort_values('Sum', ascending=False) # 'Sum' 기준 내림차순
    fig = px.bar(df, x='lang', y='Sum') # x, y 설정
    st.plotly_chart(fig) # 차트 출력
```