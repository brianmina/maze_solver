
from graphics import Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        #initialize walls
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        #Initialize positions
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2 

        #Initialize window (check the __win)
        self._win = window
    
    def draw(self):
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall, "black")

        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall, "black")

        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall, "black")

        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall, "black")