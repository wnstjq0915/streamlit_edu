import streamlit as st

from app_image import run_app_image
from app_csv import run_app_csv
from app_about import run_app_about


def main():
    st.title('앱 대시보드')

    menu = ['이미지 업로드', 'csv 업로드', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)
    # print(choice) # choice는 menu항목 중 하나가 할당됨.


    if choice == menu[0]:
        st.subheader('이미지 파일 업로드')
        run_app_image()


    elif choice == menu[1]:
        st.subheader('csv 파일 업로드')
        run_app_csv()

    elif choice == menu[2]:
        st.subheader('이 대시보드 설명')
        run_app_about()


if __name__ == '__main__':
    main()