from tkinter import Tk, BOTH, Canvas

class Windows:
    def __init__(self, width, height):
        # Create the root widget
        self.__root = Tk()

        #Set the title of the window
        self.__root.title("My window")

        #Create the canvas with the given width and height
        self.__canvas = Canvas(self.__root, width=width, height=height)

        #Pack the canvas to make it ready for drawing
        self.__canvas.pack(fill=BOTH, expand=1)

        #Initialize the running state
        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__running = False
    

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_A, point_B):
        self.point_A = point_A
        self.point_B = point_B

    def draw(self, canvas, fill_color):
        x1, y1 = self.point_A.x, self.point_A.y
        x2, y2 = self.point_B.x, self.point_B.y
        print(f'Drawing line from ({x1}, {y1}) to ({x2}, {y2}) with color {fill_color}')  # Debug
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)



    