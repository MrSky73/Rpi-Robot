import tkinter as tk
from presentation.UseCase import UseCase

class CircularButtons(tk.Canvas):
    def __init__(self, 
                 parent, 
                 callback=None,
                 button_name = "test", 
                 width =0, 
                 height =0, 
                 relx =0, 
                 rely =0, 
                 button_colour = "white", 
                 border_colour = "black"
                 ):
        super().__init__(parent,width=width, height=height, bg=button_colour, highlightthickness=0)
        self.callback = callback

        # canvas_b = tk.Canvas(self.root, width=width, height=height, bg=button_colour, highlightthickness=0)
        # canvas_b.place(relx=relx, y=rely)
        self.create_oval(5, 5, 45, 45, fill=button_colour)
        self.bind("<Button-1>", lambda e: UseCase.button_callback(button_name))
