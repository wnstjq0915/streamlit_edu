import streamlit as st
from datetime import datetime
from app_utils import save_uploaded_file

def run_app_image():
    img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])
    if img_file is not None:
        current_time = datetime.now()
        print(current_time.isoformat().replace(':', '_') + '.jpg')
        file_name = current_time.isoformat().replace(':', '_') + '.jpg'


        img_file.name = file_name
        save_uploaded_file('image', img_file)
        st.image('image/'+file_name, use_column_width=True)
