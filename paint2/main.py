from tkinter import *
from tkinter import colorchooser
from random import randint
from PIL import Image, ImageGrab
import time

# Починить масштабирование внутри PhotoImage
# Добавить вставку текста
# Добавить фильтры
# Добавить начальное окно для выбора размера изображения
# Починить ластик
# Добавить алгоритм отрисовки окружности при изменении размера карандаша
# Добавить алгоритм отрисовки пиксельной линии

canvas_width = 1280
canvas_height = 720
brush_size = 5
color = 'black'
lx = []
ly = []
lcolor = 'black'
pixel_flag = False

def paint(event):
    global brush_size
    global color
    if (pixel_flag == False):
        x1 = event.x - brush_size
        x2 = event.x + brush_size
        y1 = event.y - brush_size
        y2 = event.y + brush_size
        field.create_oval(x1, y1, x2, y2, fill=color, outline=color)
        lx.append(event.x)
        ly.append(event.y)
        if len(lx) == 2:
            cr_line()
    else:
        img.put(color, to=(event.x,event.y))

def cr_line():
    field.create_line(lx[0],ly[0],lx[1],ly[1],fill=color, width=brush_size*2)
    lx.remove(lx[0])
    ly.remove(ly[0])

def brelease(event):
    lx.clear()
    ly.clear()

def size_change (new_size):
    global brush_size
    brush_size = int(new_size)

def color_change ():
    global color
    global lcolor
    (rgb, hx) = colorchooser.askcolor()
    color = hx
    lcolor = color

def clear_canvas():
    field.delete('all')
    field['bg'] = 'white'

def pour():
    field.delete('all')
    field['bg'] = color

def eraser():
    global color
    color = 'white'

def brush():
    delbind()
    rebind()
    global color
    color = lcolor
    global pixel_flag
    pixel_flag = False

def save_img():
    time.sleep(1)
    xs = root.winfo_rootx()+field.winfo_x()
    ys = root.winfo_rooty()+field.winfo_y()
    x1 = xs + field.winfo_width()
    y1 = ys + field.winfo_height()
    img = ImageGrab.grab((xs,ys,x1,y1))
    filename = f'image_{randint(0,10000)}.png'
    img.save(filename)

def pixel_brush():
    delbind()
    rebind()
    global pixel_flag
    pixel_flag = True

def counter():
    field.itemconfigure("qwerty",image=img)
    field.after(1,counter)

def hand():
    delbind()
    field.bind("<MouseWheel>", do_zoom)
    field.bind('<ButtonPress-1>', lambda event: field.scan_mark(event.x, event.y))
    field.bind("<B1-Motion>", lambda event: field.scan_dragto(event.x, event.y, gain=1))

def do_zoom(event):
    xz = field.canvasx(event.x)
    yz = field.canvasy(event.y)
    factor = 1.001 ** event.delta
    field.scale('all', xz, yz, factor, factor)
    field.configure(scrollregion=field.bbox('all'))

def rebind():
    field.bind("<ButtonPress>", paint)
    field.bind("<B1-Motion>", paint)
    field.bind("<ButtonRelease>", brelease)

def delbind():
    field.unbind("<ButtonPress>")
    field.unbind("<B1-Motion>")
    field.unbind("<ButtonRelease>")
    field.unbind('<ButtonPress-1>')
    field.unbind("<MouseWheel>")

root = Tk()
root.title('Paint')
root.resizable(0,0)

root.option_add("*tearOff", FALSE)

field = Canvas(root, width=canvas_width, height=canvas_height, highlightthickness=0, background='white')
rebind()
field.grid(row = 0, column=0, columnspan=1, padx=1, pady=1, sticky=E+W+S+N)
image1 = Image.new("RGB",(canvas_width,canvas_height))
img = PhotoImage(width=canvas_width,height=canvas_height)
field.create_image(0,0,anchor=NW, image=img, tag="qwerty")

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="Создать") # не сделано
file_menu.add_command(label="Сохранить", command=lambda: save_img())
file_menu.add_command(label="Открыть") # не сделано

brush_menu = Menu()
brush_menu.add_command(label="Кисть", command=lambda: brush())
brush_menu.add_command(label="Ластик", command=lambda: eraser())
brush_menu.add_command(label="Карандаш", command=lambda: pixel_brush()) # доработать
brush_menu.add_command(label="Рука", command=lambda: hand()) # переделать
brush_menu.add_command(label="Текст") # не сделано

size_menu = Menu()
size_menu.add_command(label="5px", command=lambda: size_change(5))
size_menu.add_command(label="10px", command=lambda: size_change(10))
size_menu.add_command(label="15px", command=lambda: size_change(15))
size_menu.add_command(label="20px", command=lambda: size_change(20))
size_menu.add_command(label="25px", command=lambda: size_change(25))

col_menu = Menu()
col_menu.add_command(label="Выбор цвета", command=lambda: color_change())
col_menu.add_separator()
col_menu.add_command(label="Обесцвечивание") # не сделано

bgcol_menu = Menu()
bgcol_menu.add_command(label="Выбор цвета", command=lambda: pour())
bgcol_menu.add_separator()
bgcol_menu.add_command(label="Очистка холста", command=lambda: clear_canvas())

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Инструмент", menu=brush_menu)
main_menu.add_cascade(label="Толщина Кисти", menu=size_menu)
main_menu.add_cascade(label="Цвет Кисти", menu=col_menu)
main_menu.add_cascade(label="Цвет Фона", menu=bgcol_menu)

root.config(menu=main_menu)

counter()
root.mainloop()