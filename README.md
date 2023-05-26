# Download de Vídeos do YouTube

Este é um aplicativo Streamlit para download de vídeos do YouTube. Permite que você faça o download de vídeos do YouTube fornecendo um arquivo de texto com os links dos vídeos.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- Streamlit
- pytube

Você pode instalá-las executando o seguinte comando:
```
pip install streamlit pytube
```

## Como executar o aplicativo

1. Faça o clone deste repositório ou baixe o arquivo `youtube.py` para sua máquina.

2. No diretório em que o arquivo `youtube.py` está localizado, abra o terminal ou prompt de comando.

3. Execute o seguinte comando para iniciar o aplicativo:

```
streamlit run youtube.py
```

4. O aplicativo será aberto em seu navegador padrão.

## Como usar o aplicativo

1. Após abrir o aplicativo no navegador, você verá um título e uma descrição informando que você deve fazer o upload de um arquivo de texto contendo os links dos vídeos do YouTube para iniciar o download.

2. Clique no botão "Selecione um arquivo de texto" para fazer o upload do arquivo de texto. Certifique-se de que o arquivo de texto contenha um link de vídeo por linha.

3. Após selecionar o arquivo de texto, você será solicitado a fornecer o caminho onde os arquivos serão salvos. Digite o caminho completo do diretório em que você deseja salvar os vídeos baixados. Certifique-se de que o caminho seja válido e existente.

4. Após selecionar o arquivo de texto e fornecer o caminho de destino, o download dos vídeos começará automaticamente. O progresso do download será exibido no aplicativo, indicando o número do vídeo atual e o número total de vídeos a serem baixados.

5. Após o download de todos os vídeos ser concluído, uma mensagem de sucesso será exibida.

## Observações

- Certifique-se de ter uma conexão estável com a Internet para que o download dos vídeos seja realizado sem problemas.

- Os vídeos são baixados com a maior resolução disponível usando a biblioteca `pytube`.

- O aplicativo foi desenvolvido utilizando a biblioteca `streamlit` para criação da interface.

- Em caso de erros durante o download, uma mensagem de erro será exibida no aplicativo com informações sobre o problema encontrado.

