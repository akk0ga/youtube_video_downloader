from pytube import YouTube


class Video:
    def __init__(self):
        self.__url: str = ''
        self.__video: YouTube or None = None
        self.__resolution: str or None = None

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
        pass

    def _get_video_resolution(self) -> list:
        get_video_option = self.video.streams.filter(file_extension='mp4')
        resolution = []

        for stream in get_video_option:
            # print(stream)
            if not stream.resolution in resolution and stream.resolution is not None:
                resolution.append(stream.resolution)

        resolution.sort()
        return resolution

    def _download_video(self):
        print('dl video')

    def _download_video_audio(self):
        print('dl audio')

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

    def set_resolution(self, resolution: str):
        self.__resolution = resolution

    def get_resolution(self):
        return self.resolution

    url = property(fget=get_url, fset=set_url)
    video = property(fget=get_video, fset=set_video)
    resolution = property(fget=get_resolution, fset=set_resolution)
