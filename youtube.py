import streamlit as st
from pytube import YouTube

def generate_download_link(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        download_link = video.url
        return download_link
    except Exception as e:
        st.error(f"An error occurred while generating the video download link: {str(e)}")
        return None

def download_video(url, output_path):
    try:            
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(output_path=output_path)
        st.success("Download complete.")
    except Exception as e:
        st.error(f"An error occurred while downloading the video: {str(e)}")

def download_videos_from_file(file_path, output_path, is_local):
    try:
        with open(file_path, 'r') as file:
            links = file.readlines()
            links = [link.strip() for link in links if link.strip()]
            total_videos = len(links)
            for i, link in enumerate(links, start=1):
                st.write(f"Downloading video {i} of {total_videos}")
                if is_local and output_path:
                    download_video(link, output_path)
                else:
                    download_link = generate_download_link(link)
                    if download_link:
                        st.write(f"Download link: {download_link}")
    except Exception as e:
        st.error(f"An error occurred while reading the file: {str(e)}")

def main():
    st.title("YouTube Video Downloader")
    is_local = st.checkbox("I'm running locally.")
    st.write("Upload a text file containing the links (separated by lines) of YouTube videos to initiate the download.")
    output_path = None
    file = st.file_uploader("Select a text file.", type=['txt'])
 
    if is_local:
        output_path = st.text_input("Enter the path where the files will be saved.")
    if file is not None:
        file_path = file.name
        with open(file_path, 'wb') as f:
            f.write(file.getvalue())

        download_videos_from_file(file_path, output_path, is_local)
    

if __name__ == '__main__':
    main()
