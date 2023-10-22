import tkinter as tk
from presentation.UseCase import UseCase

class RectangularButton(tk.Canvas):
    def __init__(self, 
                 parent, 
                 callback=None,
                 button_name= "test",
                 width =1,
                 height =1,
                 relx =1,
                 rely =1
                 ):
        super().__init__(parent,width=width,height=height)
        self.callback = callback

        self.btn = tk.Button(
            self, 
            text=button_name, 
            width=width, 
            height=height,
            bg ="black",
            command=lambda: UseCase.button_callback(button_name)
            )
        self.btn.place(relx=relx, y = rely, anchor="ne")
