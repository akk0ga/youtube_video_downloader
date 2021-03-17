from pytube import YouTube


class Video:
    def __init__(self):
        self.__url: str = ''
        self.__video: YouTube or None = None

    def _get_title(self) -> str:
        """
        return the video title
        :return:
        """
        title = self.__video.title
        return title

    def _get_thumbnail(self):
        """
        return the video thumbnail
        :return:
        """
        thumbnail = self.__video.thumbnail_url
        return thumbnail

    def _get_video_resolution(self) -> list:
        """
        create list of resolution
        :return:
        """
        get_video_option = self.video.streams.filter(file_extension='mp4', progressive=True)
        resolution = []

        for stream in get_video_option:
            if stream.resolution not in resolution and stream.resolution is not None:
                resolution.append(stream.resolution)

        resolution.sort()
        return resolution

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
