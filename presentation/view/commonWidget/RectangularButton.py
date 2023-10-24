import tkinter as tk
import customtkinter as ctk
from presentation.UseCase import UseCase

class RectangularButton(ctk.CTkButton):
    def __init__(
            self, 
            parent,
            width=120,
            height=32,
            border_width=0,
            corner_radius=2,
            text="Button", 
            command=None, 
            **kwargs
                  ):
        super().__init__(
            parent, 
            width=width,
            height=height,
            border_width=border_width,
            corner_radius=corner_radius,
            text=text, 
            command=command, 
            **kwargs)
