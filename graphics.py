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




    