# add pytube
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from PIL import Image, ImageTk

from pytube import exceptions
from pytube import YouTube

from video.Video import Video
from downloader.Downloader import Downloader

import requests


class App(Video):
    def __init__(self):
        super().__init__()
        self.app = Tk()
        self.app_width = 800
        self.app_height = 600
        self.title = 'Youtube video downloader'

        self.app.title(self.title)
        self.app.geometry('800x600')
        self.app.configure(bg='#f1faee')
        self.app.resizable(False, False)
        self.app.iconbitmap('img/logo.ico')

    """
    ==========================================
    app info
    ==========================================
    """

    def __display_title(self) -> None:
        # display app title
        title = Label(self.app, border=None, font='Terminal 15 bold', bg='#f1faee', fg='#e63946', text=self.title)
        title.place(x=270, y=20)

    def __display_logo(self) -> None:
        # get and resize the image
        get_image = Image.open("img/logo.png")
        resize_image = get_image.resize((32, 32))
        # load image
        render = ImageTk.PhotoImage(resize_image)
        # create the image container
        logo = Label(self.app, border=None, bg='#f1faee', image=render)
        # insert the image in container
        logo.image = render
        logo.place(x=540, y=15)

    def __url_field(self) -> Entry:
        # display entry where put the link
        link = Entry(self.app, border=None, width=70)
        link.insert(0, 'url')
        x_center = (self.app_width / 4)
        link.place(x=x_center, y=500)
        return link

    """
    ==========================================
    display video info
    ==========================================
    """

    def __display_video_title(self, video: Video) -> None:
        """
        display video title
        :param video:
        :return:
        """
        video_title = video._get_title()

        if len(video_title) <= 60:
            max_char = 0
            x = self.app_width // 6
            y = 300
        else:
            max_char = 450
            x = self.app_width // 3.5
            y = 250

        title = Label(self.app, border=None, font='Terminal 15 bold', bg='#f1faee', fg='#e63946',
                      text=video_title, wraplength=max_char)
        title.place(x=x, y=y)

    def __display_video_thumbnail(self, video: Video) -> None:
        """
        display the video thumbnail
        :param video:
        :return:
        """
        # get the image from url
        get_image = requests.get(video._get_thumbnail(), stream=True).raw
        # load and resize the image retrieve
        load_image = Image.open(get_image)
        resize_image = load_image.resize((300, 150))
        # create the container for image
        image = ImageTk.PhotoImage(resize_image)
        thumbnail = Label(self.app, border=None, bg='#f1faee', image=image)
        # place the image
        x_center = (self.app_width / 2) - (image.width() / 2)
        thumbnail.image = image
        thumbnail.place(x=x_center, y=330)

    """
    ==========================================
    select resolution and path
    ==========================================
    """
    def __select_resolution_and_download(self, resolution: list, video: YouTube) -> None:
        """
        download the video with the chosen resolution
        :param resolution:
        :return:
        """
        def __download(video: YouTube) -> None:
            """
            execute when trigger dl button
            :return:
            """
            value = clicked.get()
            if value != '0' or value != 'off':
                extension = 'mp3' if value == 'audio'else 'mp4'
                dl = Downloader(extension=extension, resolution=clicked.get(), path=filedialog.askdirectory(),
                                video=video)
                dl.download()
            else:
                messagebox.showinfo('No resolution selected', 'Please select resolution')

        # create checkbox var type and title
        clicked = StringVar(value=0)
        checkbox_title = Label(self.app, border=None, font='Terminal 15 bold', bg='#f1faee', fg='#457b9d', text='Select Resolution')
        checkbox_title.place(x=310, y=70)

        # create video resolution checkbox
        x = (self.app_width // 2) - len(resolution)
        for res in resolution:
            Checkbutton(self.app, variable=clicked, onvalue=res, offvalue='off', bg='#f1faee', text=res).place(x=x, y=100)
            x += 100

        # create audio only choice
        Checkbutton(self.app, variable=clicked, onvalue='audio', offvalue='off', bg='#f1faee', text='audio only')\
            .place(x=self.app_width // 2, y=150)

        # display dl button
        button = Button(self.app, text='Download', width=50, bg='#e63946', fg='#ffffff', font='Terminal 15 bold',
                        activebackground='#e63946', activeforeground='#ffffff',
                        command=lambda: __download(video=video))
        button.place(x=130, y=550)

    """
    ==========================================
    display video info
    ==========================================
    """

    def __button_get_video_infos(self, url: Entry) -> None:
        """
        buttnon to get infos from video
        :param url:
        :return:
        """
        button = Button(self.app, text='Show infos', width=50, bg='#e63946', fg='#ffffff', font='Terminal 15 bold',
                        activebackground='#e63946', activeforeground='#ffffff',
                        command=lambda: self.__display_video_infos(url, button))
        button.place(x=130, y=550)

    def __display_video_infos(self, url: Entry, button_get_video_info: Button) -> None:
        """
        download video infos video and display checkbox
        :return:
        """
        try:
            # get url and create video instance
            url = url.get()
            video: Video = Video()

            # set value
            video.url = url
            video.video = YouTube(url)

            # display video title and thumbnail
            self.__display_video_title(video)
            self.__display_video_thumbnail(video)

            # get and launch function to select resolution
            resolution = video._get_video_resolution()
            self.__select_resolution_and_download(resolution, video.video)

            # destroy button to show infos
            button_get_video_info.destroy()
        except exceptions.RegexMatchError:
            messagebox.showwarning(title='Incorrect url', message=f"the url is incorrect")
        except exceptions.VideoPrivate:
            messagebox.showwarning(title='Private video', message=f"the video is private")
        except exceptions.VideoUnavailable:
            messagebox.showwarning(title='Unvailable video', message=f"this video is unavailable in your country")

    def run(self):
        self.__display_logo()
        self.__display_title()
        self.__button_get_video_infos(self.__url_field())
        self.app.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
