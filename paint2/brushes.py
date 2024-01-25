from tkinter import colorchooser


class Brush():


    def __init__(self):
        self.lx = []
        self.ly = []
        self.brush_size = 5
        self.color = 'black'
        self.lcolor = 'black'
        self.pixel_flag = False
        print(type(self.brush_size))
        print(type(self.lx))





    def eraser(self):
        """Меняет цвет кисти на белый."""
        self.color = 'white'


    def brush(self):
        """Выбирает режим 'кисть' для функции paint()."""
        self.color = self.lcolor
        self.pixel_flag = False

    def pixel_brush(self):
        """Выбирает режим 'карандаш' для функции paint()."""
        self.color = self.lcolor
        self.pixel_flag = True

    def size_change(self,new_size):
        """Меняет размер кисти на выбранный;
        new_size - радиус круга из функции paint()."""
        self.brush_size = int(new_size)

    def color_change(self):
        """Меняет цвет на выбранный."""
        (rgb, hx) = colorchooser.askcolor()
        self.color = hx
        self.lcolor = self.color

    def clear_canvas(self,f):
        """Полностью очищает canvas, устанавливает белый фон."""
        f.delete('all')
        f['bg'] = 'white'

    def pour(self,f):
        """Полностью очищает canvas, устанавливает фон с таким же цветом, как и у кисти."""
        f.delete('all')
        f['bg'] = self.color


