from tkinter import *
from PIL import ImageGrab
import time

class Inter():

    def save_img(self,name,r,f):
        """Высчитывает координаты холста и сохраняет изображение скриншотом в формате PNG"""
        xs = r.winfo_rootx() + f.winfo_x()
        ys = r.winfo_rooty() + f.winfo_y()
        x1 = xs + f.winfo_width()
        y1 = ys + f.winfo_height()
        img = ImageGrab.grab((xs, ys, x1, y1))
        filename = name
        time.sleep(1)
        img.save(str(filename) + '.png', 'PNG')

    def open_img(self,name,r):
        """Открывает изображение, выбранное пользователем, в формате PNG. Пересоздает окно."""
        from mwindow import Mainwindow
        m = Mainwindow()
        global new_w, new_h
        global img
        toImg = name
        if not toImg: return
        self.w_and_h(toImg)
        r.destroy()
        m.create_root(new_w, new_h, False, toImg)

    def w_and_h(self,fname):
        """Узнает размеры, открываемого изображения;
        fname - путь к изображению."""
        global new_w, new_h
        tempimg = PhotoImage(file=fname)
        new_w = tempimg.width()
        new_h = tempimg.height()

    def createImg(self,r):
        '''Запускает начальное окно.'''
        from fwindow import FirstWindow
        f = FirstWindow()
        r.destroy()
        f.firstroot()
