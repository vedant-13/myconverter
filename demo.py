import streamlit as st
from moviepy.editor import *

def main():
    st.title("MP4 to MP3 Converter")
    
    uploaded_file = st.file_uploader("Choose a video file", type="mp4")
    
    if uploaded_file is not None:
        # Write out the uploaded file to the current directory.
        with open('temp.mp4', 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        # Now you can use the filename 'temp.mp4' with VideoFileClip
        video = VideoFileClip('temp.mp4')
        video.audio.write_audiofile("out.mp3")
        st.audio('out.mp3', format='audio/mp3')

if __name__ == "__main__":
    main()
