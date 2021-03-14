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

    def __display_logo(self):
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

    def __url_field(self):
        # display entry where put the link
        link = Entry(self.app, border=None, width=70)
        link.insert(0,
                    'https://www.youtube.com/watch?v=vWAC8Wkt9ok&ab_channel=STUDIOCHOOM%5B%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4%EC%B6%A4%5D')
        x_center = (self.app_width / 4)
        link.place(x=x_center, y=500)
        return link

    def __display_video_title(self, video: Video):
        """
        display video title
        :param video:
        :return:
        """
        video_title = video._get_title()

        if len(video_title) <= 60:
            max_char = 0
            x = self.app_width // 6
            y = 350
        else:
            max_char = 450
            x = self.app_width // 3.5
            y = 300

        title = Label(self.app, border=None, font='Terminal 15 bold', bg='#f1faee', fg='#e63946',
                      text=video_title, wraplength=max_char)
        title.place(x=x, y=y)

    def __display_video_thumbnail(self, video: Video):
        """
        display the video thumbnail
        :param video:
        :return:
        """
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
        thumbnail.place(x=x_center, y=380)

    def __display_dropdown_resolution(self, resolution: list, video: Video):
        """
        create dropdown to select the video resolution
        :param resolution:
        :param video:
        :return:
        """
        def selected():
            print(clicked.get())

        clicked = StringVar()
        clicked.set(resolution[0])

        dropdown = OptionMenu(self.app, clicked, *resolution)
        dropdown.place(x=100, y=100)

        button = Button(self.app, text='Select resolution', width=50, bg='#e63946', fg='#ffffff', font='Terminal 15 bold',
                        activebackground='#e63946', activeforeground='#ffffff',
                        command=selected)
        button.place(x=130, y=550)

    def __button_dl(self, url: Entry):
        """
        butty
        :param url:
        :return:
        """
        button = Button(self.app, text='Show infos', width=50, bg='#e63946', fg='#ffffff', font='Terminal 15 bold',
                        activebackground='#e63946', activeforeground='#ffffff',
                        command=lambda: self.__download(url, button))
        button.place(x=130, y=550)

    def __download(self, url: Entry, button: Button):
        """
        download video infos video and display checkbox
        :return:
        """
        try:
            url = url.get()
            video: Video = Video()

            video.url = url
            video.video = YouTube(url)

            self.__display_video_title(video)
            self.__display_video_thumbnail(video)

            resolution = video._get_video_resolution()
            self.__display_dropdown_resolution(resolution, video)
            button.destroy()

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
