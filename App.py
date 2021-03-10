from tkinter import *
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.app = Tk()
        self.app_width = 800
        self.app_height = 600
        self.app.title('Youtube video downloader')
        self.app.geometry('800x600')
        self.app.configure(bg='#f1faee')

    def run(self):
        # display logo
        load = Image.open("img/logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self.app, border=None, bg='#f1faee', image=render)
        img.place(x=0, y=0)

        self.app.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
