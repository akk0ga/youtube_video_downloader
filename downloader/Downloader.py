from pytube import exceptions
from pytube import YouTube
from tkinter import messagebox


class Downloader:
    def __init__(self, extension: str, resolution: str, path: str, video: YouTube):
        self.__resolution: str = resolution
        self.__path: str = path
        self.__video: YouTube = video
        self.__extension = extension

    def download(self):
        fps: int = 0
        only_audio = self.__extension == 'mp3' if False else True
        print(only_audio)
        for element in self.__video.streams.filter(file_extension='mp4', resolution=self.__resolution,
                                                   progressive=True, only_audio=only_audio):
            if fps < element.fps:
                fps = element.fps
            print(element)

        # download video
        video_format = self.__video.streams.filter(file_extension='mp4', resolution=self.__resolution,
                                                   progressive=True, only_audio=only_audio).first()

        video_format.download(output_path=self.__path)
        messagebox.showinfo(title='Download success !', message=f"the video: {self.__video.title} is downloaded")
