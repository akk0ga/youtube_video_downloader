from pytube import YouTube


class Video:
    def __init__(self):
        self.__url: str
        self.__video: YouTube

    def _get_video_title(self) -> str:
        pass

    
    """
    ===================================
    getter & setter
    ===================================
    """
    def set_url(self, url: str):
        self.__url = url

    def get_url(self):
        return self.__url

    def set_video(self, video: YouTube):
        self.__video = video

    def get_video(self):
        return self.__video

    url = property(fget=get_url, fset=set_url)
    video = property(fget=get_video, fset=set_video)
