import streamlit as st
from pytube import YouTube

def generate_download_link(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        download_link = video.url
        return download_link
    except Exception as e:
        st.error(f"Ocorreu um erro ao gerar o link de download do vídeo: {str(e)}")
        return None

def download_video(url, output_path, is_local):
    try:
        download_link = generate_download_link(url)
        if download_link:
            st.markdown(f"Download link: [{download_link}]({download_link})")
            if is_local:
                youtube = YouTube(url)
                video = youtube.streams.get_highest_resolution()
                video.download(output_path=output_path)
                st.success("Download completo.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao baixar o vídeo: {str(e)}")

def download_videos_from_file(file_path, output_path, is_local):
    try:
        with open(file_path, 'r') as file:
            links = file.readlines()
            links = [link.strip() for link in links if link.strip()]
            total_videos = len(links)
            for i, link in enumerate(links, start=1):
                st.write(f"Baixando vídeo {i} de {total_videos}")
                download_video(link, output_path, is_local)
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo: {str(e)}")

def main():
    st.title("Download de Vídeos do YouTube")
    st.write("Faça o upload de um arquivo de texto contendo os links dos vídeos do YouTube para iniciar o download.")

    file = st.file_uploader("Selecione um arquivo de texto", type=['txt'])
    is_local = st.checkbox("Estou rodando localmente")
    if is_local:
        output_path = st.text_input("Informe o caminho onde os arquivos serão salvos")
    
    if file is not None and output_path:
        file_path = file.name
        with open(file_path, 'wb') as f:
            f.write(file.getvalue())

        download_videos_from_file(file_path, output_path, is_local)

if __name__ == '__main__':
    main()
