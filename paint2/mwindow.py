from tkinter import *
from tkinter import filedialog
from brushes import Brush
from fwindow import FirstWindow
from interaction import Inter

b = Brush()
f = FirstWindow()
it = Inter()


class Mainwindow():

    def create_root(self, cwidth, cheight, fo, sImg):
        """Создает окно, canvas и элементы меню;
        cwidth - ширина окна;
        cheight - высота окна;
        sImg - путь к изображению."""
        global field
        global root
        global img
        root = Tk()
        root.title('Paint')
        root.resizable(False, False)

        root.option_add("*tearOff", FALSE)

        if fo == True:
            img = PhotoImage(width=cwidth, height=cheight)
        else:
            img = PhotoImage(width=cwidth, height=cheight, file=sImg)
        field = Canvas(root, width=cwidth, height=cheight, highlightthickness=0, background='white')
        field.bind("<ButtonPress>", self.paint)
        field.bind("<B1-Motion>", self.paint)
        field.bind("<ButtonRelease>", self.brelease)
        field.grid(row=0, column=0, columnspan=1, padx=1, pady=1, sticky=E + W + S + N)
        field.create_image(0, 0, anchor=NW, image=img)  # , tag="qwerty")

        main_menu = Menu()

        file_menu = Menu()
        file_menu.add_command(label="Создать", command=lambda: it.createImg(root))
        file_menu.add_command(label="Сохранить",
                              command=lambda: it.save_img(filedialog.asksaveasfilename(filetypes=[("PNG", ".png")]),root,field))
        file_menu.add_command(label="Открыть",
                              command=lambda: it.open_img(filedialog.askopenfilename(filetypes=[("PNG", ".png")]),root))

        brush_menu = Menu()
        brush_menu.add_command(label="Кисть", command=lambda: b.brush())
        brush_menu.add_command(label="Ластик", command=lambda: b.eraser())
        brush_menu.add_command(label="Карандаш", command=lambda: b.pixel_brush())  # доработать
        # brush_menu.add_command(label="Рука", command=lambda: hand()) # переделать
        # brush_menu.add_command(label="Текст")  # не сделано

        size_menu = Menu()
        size_menu.add_command(label="5px", command=lambda: b.size_change(5))
        size_menu.add_command(label="10px", command=lambda: b.size_change(10))
        size_menu.add_command(label="15px", command=lambda: b.size_change(15))
        size_menu.add_command(label="20px", command=lambda: b.size_change(20))
        size_menu.add_command(label="25px", command=lambda: b.size_change(25))

        col_menu = Menu()
        col_menu.add_command(label="Выбор цвета", command=lambda: b.color_change())
        col_menu.add_separator()
        # col_menu.add_command(label="Негатив", command=lambda: negImg())

        bgcol_menu = Menu()
        bgcol_menu.add_command(label="Цвет холста", command=lambda: b.pour(field))
        bgcol_menu.add_command(label="Очистка холста", command=lambda: b.clear_canvas(field))

        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Инструмент", menu=brush_menu)
        main_menu.add_cascade(label="Толщина Кисти", menu=size_menu)
        main_menu.add_cascade(label="Цвет", menu=col_menu)
        main_menu.add_cascade(label="Холст", menu=bgcol_menu)

        root.config(menu=main_menu)
        root.mainloop()

    def paint(self,event):
        """Рисует круг (или ставит пиксель, если выбран инструмент 'карандаш') на холсте, при зажатой левой кнопки мыши;
        event - произошедшее событие."""
        if event.x >= 0 and event.y >= 0:
            if (b.pixel_flag == False):
                x1 = event.x - b.brush_size
                x2 = event.x + b.brush_size
                y1 = event.y - b.brush_size
                y2 = event.y + b.brush_size
                field.create_oval(x1, y1, x2, y2, fill=b.color, outline=b.color)
                b.lx.append(event.x)
                b.ly.append(event.y)
                if len(b.lx) == 2:
                    self.cr_line()
            else:
                img.put(b.color, to=(event.x, event.y))

    def cr_line(self):
        """Рисует линию, которая соединяет два круга, созданных в функции paint(). Координаты для линии берутся из списков
        lx и ly."""
        field.create_line(b.lx[0], b.ly[0], b.lx[1], b.ly[1], fill=b.color, width=b.brush_size * 2)
        b.lx.remove(b.lx[0])
        b.ly.remove(b.ly[0])

    def brelease(self,event):
        """Удаляет элементы из списков с координатами для линий, если левая кнопка мыши отжата;
        event - произошедшее событие."""
        b.lx.clear()
        b.ly.clear()





