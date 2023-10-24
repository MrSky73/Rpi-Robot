import tkinter as tk
from tkinter import PhotoImage
import customtkinter as ctk

class ImageButton(tk.Button):
    def __init__(self, parent, image_path, bg = "white", fg= "white",zoom = 5, subSample = 50, command=None, **kwargs):
        super().__init__(parent, bg = "white", fg= "white", **kwargs)

        self.image = PhotoImage(file = image_path)
        self.icon = self.image.zoom(zoom).subsample(subSample)
        self.configure(image=self.icon, command=command)