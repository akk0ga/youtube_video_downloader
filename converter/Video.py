from pytube import YouTube


class Video:
    def __init__(self):
        self.__url: str = ''
        self.__video: YouTube or None = None

    def _get_title(self) -> str:
        """
        TODO
            get the title of video
        return the video title
        :return:
        """
        title = self.__video.title
        return title

    def _get_thumbnail(self):
        """
        TODO
            get the video thumbnail
        return the video thumbnail
        :return:
        """
        thumbnail = self.__video.thumbnail_url
        return thumbnail
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
        if self.__video is None:
            return 'No video loaded'
        else:
            return self.__video

    url = property(fget=get_url, fset=set_url)
    video = property(fget=get_video, fset=set_video)
