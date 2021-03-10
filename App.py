from tkinter import *


class App:
    def __init__(self):
        self.app = Tk()
        self.app.title('Youtube video downloader')
        self.app.geometry('800x600')

    def run(self):
        self.app.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
