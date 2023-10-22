import tkinter as tk
from presentation.view.commonWidget.ArrowButton import ArrowButtons

class MovementButton(tk.Canvas):
    def __init__(self, parent, command=None):
        super().__init__(parent)

        arrow_size = 50
        x_offset = 10
        y_offset = 525 - arrow_size  # Placing it slightly above the very bottom
        button_colur = "gray"


        self.right_button = ArrowButtons(
            parent=self,
            arrow_size = arrow_size,
            x_offset=x_offset,
            y_offset=y_offset,
            button_colour=button_colur,
            button_name="right",
            x0= arrow_size,
            y0= arrow_size/2,
            x1= 0,
            y1= 0,
            xy= 0,
            var=arrow_size
        )
        
        self.left_button = ArrowButtons(
            parent=self,
            arrow_size = arrow_size,
            x_offset=x_offset,
            y_offset=y_offset,
            button_colour=button_colur,
            button_name="left",
            x0= 0,
            y0= arrow_size/2,
            x1= arrow_size,
            y1= 0,
            xy= arrow_size,
            var=arrow_size
        )

        self.up_button = ArrowButtons(
            parent=self,
            arrow_size = arrow_size,
            x_offset=x_offset,
            y_offset=y_offset,
            button_colour=button_colur,
            button_name="up"
        )

        self.down_button = ArrowButtons(
            parent=self,
            arrow_size = arrow_size,
            x_offset=x_offset,
            y_offset=y_offset,
            button_colour=button_colur,
            button_name="down",
            x0= arrow_size/2,
            y0= arrow_size,
            x1= 0,
            y1= 0,
            xy= arrow_size,
            var=0
        )