import streamlit as st
from datetime import datetime
import pandas as pd
from app_utils import save_uploaded_file

def run_app_csv():
    csv_file = st.file_uploader('CSV 파일 업로드', type=['csv'])
    if csv_file is not None:
        current_time = datetime.now()
        file_name = current_time.isoformat().replace(':', '_') + '.csv'
        csv_file.name = file_name
        save_uploaded_file('csv', csv_file)

        df = pd.read_csv('csv/'+file_name)
        st.dataframe(df)
