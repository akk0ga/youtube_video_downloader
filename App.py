# add pytube
from tkinter import *
from PIL import Image, ImageTk
from converter.Video import Video


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

    def __display_title(self):
        # display app title
        title = Label(self.app, border=None, font='Terminal 15 bold', bg='#f1faee', fg='#e63946', text=self.title)
        title.place(x=270, y=50)

    def __url_field(self):
        # display entry where put the link
        link = Entry(self.app, border=None, width=70)
        link.insert(0, 'url')
        x_center = (self.app_width / 4)
        link.place(x=x_center, y=400)
        return link

    def __button_dl(self, url: Entry):
        # display button to launch dl
        button = Button(self.app, text='Download', width=50, bg='#e63946', fg='#ffffff', font='Terminal 15 bold',
                        activebackground='#e63946', activeforeground='#ffffff', command=lambda: self.__convert(url))
        button.place(x=130, y=500)

    def __convert(self, url: Entry):
        """
        convert video to the format select
        :return:
        """
        url = url.get()
        convertor = Video()

        convertor.url = url
        print(convertor.video)


    def run(self):
        # display logo
        load = Image.open("img/logo.png")
        render = ImageTk.PhotoImage(load)
        x_center = (self.app_width / 2) - (render.width() / 2)
        img = Label(self.app, border=None, bg='#f1faee', image=render)
        img.place(x=x_center, y=100)

        self.__display_title()

        url = self.__url_field()
        print(type(url))

        self.__button_dl(url)
        self.app.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
