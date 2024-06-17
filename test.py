import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        start_x = 0  # Example starting point
        start_y = 0  # Example starting point
        cell_size_x = 10  # Example cell size
        cell_size_y = 10  # Example cell size
        win = None  # Placeholder for graphical window

        m1 = Maze(start_x, start_y, num_rows, num_cols, cell_size_x, cell_size_y, win)
        
        print(f"Test Maze with 10x12 grid: {len(m1._cells)} rows and {len(m1._cells[0])} cols")
        
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_large(self):
        num_cols = 20
        num_rows = 15
        start_x = 0  # Example starting point
        start_y = 0  # Example starting point
        cell_size_x = 10  # Example cell size
        cell_size_y = 10  # Example cell size
        win = None  # Placeholder for graphical window

        m1 = Maze(start_x, start_y, num_rows, num_cols, cell_size_x, cell_size_y, win)
        
        print(f"Test Maze with 15x20 grid: {len(m1._cells)} rows and {len(m1._cells[0])} cols")
        
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

if __name__ == "__main__":
    unittest.main()