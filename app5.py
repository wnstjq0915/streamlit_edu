import streamlit as st

from PIL import Image

def main():
    st.title('웹 대시보드')

    # 사진과 영상을 보여주는 방법

    img = Image.open('data/image_03.jpg') # 이미지 불러옴.
    st.image(img) # 이미지 웹에 보여줌.

    st.image(img, use_column_width=True) # 화면 꽉 채움.

    # 이미지 URL로 불러와서 보여주기
    st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.epnc.co.kr%2Fnews%2FarticleView.html%3Fidxno%3D91021&psig=AOvVaw2Z_2UXm9QK2x5WlEJeEAeK&ust=1684978134667000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCKC18-vmjP8CFQAAAAAdAAAAABAI', use_column_width=True)
    
    video_file = open('data/video1.mp4', 'rb')
    st.video(video_file)
    # 유튜브 링크를 써서 보여주는 방법도 있음. 나중에 찾아보기.

if __name__ == '__main__':
    main()
