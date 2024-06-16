import streamlit as st 
import pandas as pd

st.subheader('Loading the CSV File ')

df = st.file_uploader("Upload the CSV file : ", type = ['csv' , 'xlsx'])

st.subheader('Loading the CSV file')
if df is not None:
    df = pd.read_csv(df)
    #st.dataframe(df)
    st.table(df.head())
    
st.subheader('Dealing with images')
img = st.file_uploader("Upload the image file :", type=['png' , 'jpeg'])
if img:
    st.image(img)

st.subheader('Working with Videos')
video_file = st.file_uploader('Upload the video file :', type = ['mkv' , 'mp4'])
if video_file :
    st.video(video_file , start_time = 0)

