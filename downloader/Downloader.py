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
        print(self.__extension)

        only_audio = True if self.__extension == 'mp3' else False
        type = 'audio' if only_audio else 'video'
        mime_type = 'audio/mp4' if type == 'audio' else 'video/mp4'

        if type == 'video':
            streams = self.__video.streams.filter(only_audio=only_audio, type=type, mime_type=mime_type, progressive=True)
            for element in streams:
                print(element)
        else:
            streams = self.__video.streams.filter(only_audio=only_audio, type=type, mime_type=mime_type)

        # download video
        streams.first().download(output_path=self.__path, filename=f'video_{self.__video.title}')
        messagebox.showinfo(title='Download success !', message=f"the video: {self.__video.title} is downloaded")
