import tkinter as tk
from tkinter import PhotoImage, filedialog
import customtkinter as ctk

class ImageButton(tk.Button):
    def __init__(self, parent, image_path, command=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.image = PhotoImage(file = image_path)
        self.icon = self.image.zoom(5).subsample(50)
        self.configure(image=self.icon, command=command)