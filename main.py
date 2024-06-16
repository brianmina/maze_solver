from graphics import Windows, Point, Line, Cell
from cell import Cell



def main():
     # Create a Window instance with a width of 800 pixels and height of 600 pixels
    window = Windows(800, 600)

    # Create Point instances
    point1 = Point(50, 50)
    point2 = Point(150, 150)
    point3 = Point(150, 50)
    point4 = Point(50, 150)

    # Create Line instances
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)

    # Draw the lines on the window's canvas
    window.draw_line(line1, "black")
    window.draw_line(line2, "red")

    # Create some cells
    cell1 = Cell(10, 10, 50, 50, window)
    cell2 = Cell(60, 10, 100, 50, window)

    # Modify walls if needed
    cell2.has_left_wall = False

    # Draw the cells
    cell1.draw()
    cell2.draw()

    # Wait for the window to close
    window.wait_for_close()

    # Ensure the main function runs when this script is executed
if __name__ == "__main__":
    main()