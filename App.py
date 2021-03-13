# add pytube
from tkinter import *
from PIL import Image, ImageTk
from pytube import exceptions
from pytube import YouTube
from converter.Video import Video
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

    def __display_title(self):
        # display app title
        title = Label(self.app, border=None, font='Terminal 15 bold', bg='#f1faee', fg='#e63946', text=self.title)
        title.place(x=270, y=20)

    def __url_field(self):
        # display entry where put the link
        link = Entry(self.app, border=None, width=70)
        link.insert(0, 'url')
        x_center = (self.app_width / 4)
        link.place(x=x_center, y=500)
        return link

    def __display_logo(self):
        # open the image and create
        render = ImageTk.PhotoImage(Image.open("img/logo.png"))
        # calc to place logo at center
        x_center = (self.app_width / 2) - (render.width() / 2)
        # create the image container
        logo = Label(self.app, border=None, bg='#f1faee', image=render)
        # insert the image in container
        logo.image = render
        logo.place(x=x_center, y=70)

    def __display_video_title(self, video: Video):
        video_title = video._get_title()

        if len(video_title) <= 60:
            max_char = 0
            x = 100
        else:
            max_char = 450
            x = self.app_width / 4

        title = Label(self.app, border=None, font='Terminal 15 bold', bg='#f1faee', fg='#e63946',
                      text=video_title, wraplength=max_char)
        print(len(video_title))
        title.place(x=x, y=210)

    def __display_video_thumbnail(self, video: Video):
        # get the image from url
        get_image = requests.get(video._get_thumbnail(), stream=True).raw
        # load and resize the image retrieve
        load_image = Image.open(get_image)
        resize_image = load_image.resize((200, 100))
        # create the container for image
        image = ImageTk.PhotoImage(resize_image)
        thumbnail = Label(self.app, border=None, bg='#f1faee', image=image)
        # place the image
        x_center = (self.app_width / 2) - (image.width() / 2)
        thumbnail.image = image
        thumbnail.place(x=x_center, y=300)

    def __button_dl(self, url: Entry):
        # display button to launch dl
        button = Button(self.app, text='Download', width=50, bg='#e63946', fg='#ffffff', font='Terminal 15 bold',
                        activebackground='#e63946', activeforeground='#ffffff', command=lambda: self.__convert(url))
        button.place(x=130, y=550)

    def __convert(self, url: Entry):
        """
        convert video to the format select
        :return:
        """
        url = url.get()
        video = Video()
        try:
            video.url = url
            video.video = YouTube(url)
            self.__display_video_title(video)
            self.__display_video_thumbnail(video)
        except exceptions.RegexMatchError:
            print('the url is not correct')
        except exceptions.VideoPrivate:
            print('Can\'t reach the video')
        except exceptions.VideoUnavailable:
            print('this video is unavailable')

    def run(self):
        self.__display_logo()
        self.__display_title()
        self.__button_dl(self.__url_field())
        self.app.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
