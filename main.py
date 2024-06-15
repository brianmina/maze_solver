from graphs import Windows



def main():
     # Create a Window instance with a width of 800 pixels and height of 600 pixels
    win = Windows(800, 600)

    # Wait for the window to close
    win.wait_for_close()

    # Ensure the main function runs when this script is executed
if __name__ == "__main__":
    main()