import streamlit as st

def main():
    st.title('웹 대시보드')

    name = st.text_input('이름을 입력하세요!', max_chars=10) # 엔터를 쳐야 저장.
    # 최대길이 10, value='기본값' 가능
    st.text(name)

    message = st.text_area('메세지를 입력하세요.', height=5) # height 찾아보기
    st.text(message)

    # 숫자 입력

    number = st.number_input('숫자를 입력하세요~', 1, 100) # min_value, max_value, step도 가능.
    # number_input 기본값 float
    st.text(number * 3)

    number2 = st.number_input('숫자를 입력하세요~', 1.0, 100.0)
    st.text(number2 * 3)

    # 날짜
    my_date = st.date_input('날짜를 입력하세요.')
    # 기본값 현재날짜, 타입은 date 타입
    st.text(my_date)

    # 시간
    my_time = st.time_input('시간 선택')
    # 디폴트 15분씩, 알아서 조정하기.
    st.text(my_time)

    # 비밀번호 처리
    password = st.text_input('비밀번호 입력', type='password')
    st.text(password)

    # 색 입력
    color = st.color_picker('색을 선택하세요.')
    st.text(color) # 헥스코드 나옴.

if __name__ == '__main__':
    main()