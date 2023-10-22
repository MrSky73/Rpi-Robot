import tkinter as tk
from presentation.UseCase import UseCase

class ImageButton(tk.Canvas):
    def __init__(self, 
                 parent, 
                 callback,
                 relx, 
                 rely, 
                 icon_address, 
                 icon_name, 
                 zoom, 
                 subsample
                 ):
        super().__init__(parent)
        self.callback = callback

        image = tk.PhotoImage(file=icon_address)
        icon = image.zoom(zoom)
        icon = image.subsample(subsample)
        # icon = image.height(10)
        # icon = image.width(10)
        btn = tk.Button(self, image=icon, command=lambda: UseCase.button_callback(icon_name))
        btn.image = icon
        btn.place(relx=relx, y=rely, anchor="ne")