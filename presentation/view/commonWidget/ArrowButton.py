import tkinter as tk
from presentation.UseCase import UseCase

class ArrowButtons(tk.Canvas):
    def __init__(self, 
                parent, 
                callback = None, 
                arrow_size = 1, 
                x_offset =0, 
                y_offset =0, 
                button_colour = "white",
                button_name = "test",
                x0=0,
                y0=0, 
                x1=0, 
                y1=0, 
                xy=0,
                var=0
        ):
        
        super().__init__(parent, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        self.callback = callback

        # canvas = tk.Canvas(self, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        # canvas.place(x=x_offset + 2*arrow_size, y=y_offset)        
        self.create_polygon(
            x0, 
            y0, 
            x1, 
            y1, 
            xy,
            var,
            fill=button_colour
        )
        self.bind("<Button-1>", lambda e: UseCase.button_callback(button_name))

    # def button_callback(self, button_name):
    #     print(f"{button_name} button pressed")

    # def on_click(self,event):
    #     if self.command
    #         self.command()
        