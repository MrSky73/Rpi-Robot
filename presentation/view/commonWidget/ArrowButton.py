import customtkinter as ctk
import tkinter as tk
from tkinter import PhotoImage

from presentation.view.commonWidget.ImageButton import ImageButton

class ArrowButton(tk.Button):
    def __init__(self, parent, direction, zoom =5, subSample=50, command=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.direction = direction

        if direction == "up":
            asset_path = f"./assets/Up.png" 
            self.image = PhotoImage(file = asset_path)
            self.icon = self.image.zoom(5).subsample(50)
            self.configure(image=self.icon, command=command)
        elif direction == "down":
            asset_path = f"./assets/Down.png" 
            self.image = PhotoImage(file = asset_path)
            self.icon = self.image.zoom(5).subsample(50)
            self.configure(image=self.icon, command=command)
        elif direction == "left":
            asset_path = f"./assets/Left.png" 
            self.image = PhotoImage(file = asset_path)
            self.icon = self.image.zoom(5).subsample(50)
            self.configure(image=self.icon, command=command)
        elif direction == "right":
            asset_path = f"./assets/Right.png"
            self.image = PhotoImage(file = asset_path)
            self.icon = self.image.zoom(5).subsample(50)
            self.configure(image=self.icon, command=command)
        else:
            raise ValueError("Invalid direction: {}".format(direction))
