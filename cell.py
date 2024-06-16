
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
    
    # def draw_move(self, to_cell, undo=False):
    #     start_x, start_y = self.x, self.y  # Get self's center coordinates
    #     end_x, end_y = to_cell.x, to_cell.y  # Get to_cell's center coordinates

    #     color = "gray" if undo else "red"  # Choose color based on undo flag

    #     # Assume self.draw_line() draws a line between two points (x1, y1) to (x2, y2) with a given color
    #     self.draw_line(start_x, start_y, end_x, end_y, color)


    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
