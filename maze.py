from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._cells = [[Cell(win) for _ in range(num_cols)] for _ in range(num_rows)]
        print(f"Initialized Maze with {len(self._cells)} rows and {len(self._cells[0])} cols")
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        print(f"Creating cells with parameters: num_rows={self._num_rows}, num_cols={self._num_cols}")
        print(f"Before creation: {len(self._cells)} rows and {len(self._cells[0])} cols")
        # Ensure this method sets up cells but does not change grid dimensions
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j] = Cell(self._win)
        print(f"After creation: {len(self._cells)} rows and {len(self._cells[0])} cols")

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)


