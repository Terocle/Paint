import tkinter
from tkinter import ttk, N



class FirstWindow():
    def firstroot(self):
        """Создает начальное окно для выбора размеров холста."""
        global froot, text1, text2
        froot = tkinter.Tk()
        froot.title('Paint')
        froot.geometry('250x230')
        froot.resizable(False, False)
        label1 = ttk.Label(text="Введите ширину (350 - 1920)", padding=(0, 20, 0, 0))
        label1.pack()
        it1 = tkinter.IntVar()
        text1 = ttk.Entry(textvariable=it1)
        text1.pack(anchor=N, padx=8, pady=8)
        label2 = ttk.Label(text="Введите высоту (350 - 1080)", padding=(0, 20, 0, 0))
        label2.pack()
        it2 = tkinter.IntVar()
        text2 = ttk.Entry(textvariable=it2)
        text2.pack(anchor=N, padx=8, pady=8)
        b1 = ttk.Button(text='Создать Холст', command=lambda: self.check_var())
        b1.pack(pady=20)
        froot.mainloop()

    def check_var(self):
        """Проверяет значения введенные пользователем."""
        t1 = text1.get()
        t2 = text2.get()
        if (int(t1) >= 350 and int(t2) >= 350) and (int(t1) <= 1920 and int(t2) <= 1080):
            self.create_newImg()
        else:
            return

    def create_newImg(self):
        """Уничтожает начальное окно и вызывает функцию создания холста с размерами, заданными пользователем."""
        from mwindow import Mainwindow
        m = Mainwindow()
        t1 = text1.get()
        t2 = text2.get()
        froot.destroy()
        m.create_root(t1, t2, True, None)