import tkinter as tk
from presentation.view.commonWidget.ArrowButton import ArrowButton

class MovementButton(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Create arrow buttons
        arrow_size = 50
        x_offset = 10
        y_offset = 525 - arrow_size

        self.up_button = ArrowButton(self, direction="up", arrow_size=arrow_size)
        self.up_button.place(x=x_offset + arrow_size, y=y_offset - arrow_size)

        self.down_button = ArrowButton(self, direction="down" ,arrow_size=arrow_size)
        self.down_button.place(x=x_offset + arrow_size, y=y_offset + arrow_size)

        self.left_button = ArrowButton(self, direction="left", arrow_size=arrow_size)
        self.left_button.place(x=x_offset, y=y_offset)

        self.right_button = ArrowButton(self, direction="right", arrow_size=arrow_size)
        self.right_button.place(x=x_offset + 2*arrow_size, y=y_offset) 

        # Position the movement button frame
        self.place(relx=0.05, rely=0.9, anchor="sw")
