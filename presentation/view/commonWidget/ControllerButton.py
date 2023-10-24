import customtkinter as ctk
import tkinter as tk
from tkinter import PhotoImage

class ControllerButton(tk.Button):
    def __init__(self, parent, direction, zoom =5, subSample=50, command=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.direction = direction

        if direction == "additon":
            asset_path = f"./assets/Addition.png" 
            self.image = PhotoImage(file = asset_path)
            self.icon = self.image.zoom(5).subsample(50)
            self.configure(image=self.icon, command=command)
        elif direction == "triangle":
            asset_path = f"./assets/Triangle.png" 
            self.image = PhotoImage(file = asset_path)
            self.icon = self.image.zoom(5).subsample(50)
            self.configure(image=self.icon, command=command)
        elif direction == "cross":
            asset_path = f"./assets/Cross.png" 
            self.image = PhotoImage(file = asset_path)
            self.icon = self.image.zoom(5).subsample(50)
            self.configure(image=self.icon, command=command)
        elif direction == "circle":
            asset_path = f"./assets/Circle.png"
            self.image = PhotoImage(file = asset_path)
            self.icon = self.image.zoom(5).subsample(50)
            self.configure(image=self.icon, command=command)
        else:
            raise ValueError("Invalid direction: {}".format(direction))

        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        print("Arrow button clicked in direction: {}".format(self.direction))

