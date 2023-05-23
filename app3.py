import streamlit as st
import pandas as pd

def main():
    st.title('웹 대시보드')

    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)

    species = df['species'].unique()
    st.text('아이리스 꽃은' + species + '으로 되어있다.')

    st.write(df.head()) # write는 다방면으로 가능.

if __name__ == '__main__':
    main()

# streamlit run app3.py