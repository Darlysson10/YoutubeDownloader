import streamlit as st
from pytube import YouTube
import pytube

def download_video(url, output_path):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(output_path=output_path)
        st.success("Download completo.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao baixar o vídeo: {str(e)}")

def download_videos_from_file(file_path, output_path):
    try:
        with open(file_path, 'r') as file:
            links = file.readlines()
            links = [link.strip() for link in links if link.strip()]
            total_videos = len(links)
            for i, link in enumerate(links, start=1):
                st.write(f"Baixando vídeo {i} de {total_videos}")
                download_video(link, output_path)
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo: {str(e)}")

def main():
    st.title("Download de Vídeos do YouTube")
    st.write("Faça o upload de um arquivo de texto contendo os links dos vídeos do YouTube para iniciar o download.")
    file = st.file_uploader("Selecione um arquivo de texto", type=['txt'])
    output_path = st.text_input("Informe o caminho onde os arquivos serão salvos")

    if file is not None and output_path:
        file_path = file.name
        with open(file_path, 'wb') as f:
            f.write(file.getvalue())

        download_videos_from_file(file_path, output_path)

if __name__ == '__main__':
    main()
