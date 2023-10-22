import tkinter as tk

class ArrowButtons(tk.Frame):
    def __init__(self, parent, callback, arrow_size, x_offset, y_offset, button_colour, button_name, x0, y0, x1, y1, xy,var):
        super().__init__(parent)
        self.callback = callback

        canvas = tk.Canvas(self, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        canvas.place(x=x_offset + 2*arrow_size, y=y_offset)        
        canvas.create_polygon(
            x0, 
            y0, 
            x1, 
            y1, 
            xy,
            var,
            fill=button_colour
        )
        canvas.bind("<Button-1>", lambda e: self.button_callback(button_name))

    # def on_click(self,event):
    #     if self.command
    #         self.command()
        