import tkinter as tk
from presentation.view.commonWidget.ArrowButton import ArrowButtons

class MovementButtons(tk.Frame):
    def __init__(self, parent, command=None):
        super().__init__(parent)

        arrow_size = 50
        x_offset = 10
        y_offset = 525 - arrow_size  # Placing it slightly above the very bottom
        button_colur = "gray"


        self.left_button = ArrowButtons(
            arrow_size = arrow_size,
            x_offset=x_offset,
            y_offset=y_offset,
            button_colour=button_colur,
            button_name="left",
            x0= arrow_size,
            y0= arrow_size/2,
            x1= 0,
            y1= 0,
            xy= 0,
            var=arrow_size
        )
        
        self.right_button = ArrowButtons(
            arrow_size = arrow_size,
            x_offset=x_offset,
            y_offset=y_offset,
            button_colour=button_colur,
            button_name="right"
            )
        
        self.up_button = ArrowButtons(
            arrow_size = arrow_size,
            x_offset=x_offset,
            y_offset=y_offset,
            button_colour=button_colur,
            button_name="up"
            )
        
        self.down_button = ArrowButtons(
            arrow_size = arrow_size,
            x_offset=x_offset,
            y_offset=y_offset,
            button_colour=button_colur,
            button_name="down"
            )

    def create_movement_buttons(self, arrow_size, x_offset, y_offset, button_colour, button_name):
        arrow_size = 50
        x_offset = 10
        y_offset = 525 - arrow_size  # Placing it slightly above the very bottom

        # Left Arrow
        left_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        left_canvas.place(x=x_offset + 2*arrow_size, y=y_offset)        
        left_canvas.create_polygon(arrow_size, arrow_size/2, 0, 0, 0, arrow_size, fill="gray")
        left_canvas.bind("<Button-1>", lambda e: self.button_callback("right"))

        # Right Arrow
        right_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        right_canvas.place(x=x_offset, y=y_offset)
        right_canvas.create_polygon(0, arrow_size/2, arrow_size, 0, arrow_size, arrow_size, fill="gray")
        right_canvas.bind("<Button-1>", lambda e: self.button_callback("left"))

        # Up Arrow
        up_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        up_canvas.place(x=x_offset + arrow_size, y=y_offset - arrow_size)
        up_canvas.create_polygon(arrow_size/2, 0, 0, arrow_size, arrow_size, arrow_size, fill="gray")
        up_canvas.bind("<Button-1>", lambda e: self.button_callback("up"))

        # Down Arrow
        down_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        down_canvas.place(x=x_offset + arrow_size, y=y_offset + arrow_size)
        down_canvas.create_polygon(arrow_size/2, arrow_size, 0, 0, arrow_size, 0, fill="gray")
        down_canvas.bind("<Button-1>", lambda e: self.button_callback("down"))
    
    def button_callback(self, button_name):
        print(f"{button_name} button pressed")