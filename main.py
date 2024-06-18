from graphics import Window
from maze import Maze


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    print(f"num_rows = {num_rows}, type(num_rows) = {type(num_rows)}")
    print(f"num_cols = {num_cols}, type(num_cols) = {type(num_cols)}")

    maze = Maze(margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)

    win.wait_for_close()


main()