# YouTube Video Downloader

This is a Streamlit application for downloading YouTube videos. It allows you to download videos from YouTube by providing a text file with the video links.

## Prerequisites

Make sure you have the following libraries installed:

- Streamlit
- pytube

You can install them by running the following command:
```
pip install streamlit
```

## How to run the application

1. Clone this repository.

2. In the directory where the `youtube.py` file is located, open the terminal or command prompt.

3. Run the following command to start the application:

```
streamlit run youtube.py
```

4. The application will open in your default browser.

## How to use the application

1. After opening the application in the browser, you will see a title and a description instructing you to upload a text file containing the YouTube video links to initiate the download.

2. Click on the "Select a text file" button to upload the text file. Make sure the text file contains one video link per line.

3. After selecting the text file, you will be prompted to provide the path where the files will be saved, if eu check "I'm running locally" box. Enter the full path of the directory where you want to save the downloaded videos. Make sure the path is valid and exists.

4. After selecting the text file and providing the destination path, the video download or link generation will start automatically. The progress will be displayed in the application, indicating the current video number and the total number of videos to be downloaded.

5. Once all the videos are downloaded, a success message will be displayed.

## Notes

- The application was developed using the `streamlit` library to create the interface.

- In case of errors during the download, an error message will be displayed in the application with information about the encountered problem.
