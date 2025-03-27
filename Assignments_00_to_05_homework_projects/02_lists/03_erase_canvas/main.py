# Import the tkinter library for creating GUI applications
import tkinter as tk

class EraserCanvas:
    """A canvas widget that allows erasing cells in a grid using a movable eraser."""
    
    def __init__(self, root, rows=10, cols=10, cell_size=60, eraser_size=60):
        # Store the main window instance for later use
        self.root = root
        # Set the number of rows in the grid (default: 10)
        self.rows = rows        
        # Set the number of columns in the grid (default: 10)
        self.cols = cols        
        # Define the size of each grid cell in pixels (default: 60px)
        self.cell_size = cell_size    
        # Define the size of the eraser tool in pixels (default: 60px)
        self.eraser_size = eraser_size    

        # Calculate total canvas dimensions based on grid size and cell size
        canvas_width = cols * cell_size
        canvas_height = rows * cell_size
        # Create a new canvas widget with white background
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
        # Display the canvas in the window using pack geometry manager
        self.canvas.pack()

        # Initialize empty list to store grid cell references
        self.cells = []
        # Call method to create the initial grid pattern
        self.draw_grid()    

        # Create the eraser tool as a rectangular shape
        # Parameters: top-left (0,0) and bottom-right coordinates
        self.eraser = self.canvas.create_rectangle(
            0, 0,                         # Initial top-left position
            eraser_size, eraser_size,     # Initial bottom-right position
            outline='black',              # Black border for eraser
            width=2                       # Border thickness
        )

        # Set up mouse event bindings
        self.canvas.bind('<B1-Motion>', self.erase)      # Drag with left mouse button
        self.canvas.bind('<Motion>', self.move_eraser)   # Any mouse movement

    def draw_grid(self):
        """Creates a grid of blue cells on the canvas."""
        # Iterate through each row
        for row in range(self.rows):
            # Create a list to store cells in current row
            row_cells = []
            # Iterate through each column in current row
            for col in range(self.cols):
                # Calculate pixel coordinates for current cell
                x1 = col * self.cell_size  # Left edge
                y1 = row * self.cell_size  # Top edge
                x2 = x1 + self.cell_size   # Right edge
                y2 = y1 + self.cell_size   # Bottom edge

                # Create a blue rectangle with black outline for current cell
                cell = self.canvas.create_rectangle(
                    x1, y1, x2, y2,         # Cell coordinates
                    fill='blue',            # Fill color
                    outline='black'          # Border color
                )
                # Add cell reference to current row
                row_cells.append(cell)
            # Add completed row to cells grid
            self.cells.append(row_cells)
    
    def erase(self, event):
        """Erases (turns white) any cells that overlap with the eraser."""
        # Find all canvas objects that intersect with eraser bounds
        overlapping = self.canvas.find_overlapping(
            event.x,                     # Left edge of eraser
            event.y,                     # Top edge of eraser
            event.x + self.eraser_size,  # Right edge of eraser
            event.y + self.eraser_size   # Bottom edge of eraser
        )
        # Process each overlapping object
        for item in overlapping:
            # Skip if the item is the eraser itself
            if item != self.eraser:
                # Change the cell color to white (erase)
                self.canvas.itemconfig(item, fill='white')
    
    def move_eraser(self, event):
        """Updates the eraser's position to follow the mouse cursor."""
        # Update eraser position to follow mouse pointer
        self.canvas.coords(
            self.eraser,                 # Eraser object
            event.x,                     # New left edge
            event.y,                     # New top edge
            event.x + self.eraser_size,  # New right edge
            event.y + self.eraser_size   # New bottom edge
        )

# Only run this code if the script is run directly (not imported)
if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    # Set the window title
    root.title("Eraser Canvas")
    # Create an instance of EraserCanvas
    app = EraserCanvas(root)
    # Start the Tkinter event loop to handle user interactions
    root.mainloop()