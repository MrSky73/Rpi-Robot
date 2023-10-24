import customtkinter as ctk
import tkinter as tk
from presentation.UseCase import UseCase

from presentation.view.commonWidget.ControllerButton import ControllerButton


class CommandButton(tk.Frame):
    def __init__(self, master, bg="white",**kwargs):
        super().__init__(master, bg="white",**kwargs)
            
        zoom =1
        subSample=1

        self.addition_button = ControllerButton(self, "additon",zoom=zoom,subSample=subSample, command=lambda event=None: UseCase.button_callback("additon"))
        self.triangle_button = ControllerButton(self, "triangle",zoom=zoom,subSample=subSample, command=lambda event=None: UseCase.button_callback("triangle"))
        self.cross_button = ControllerButton(self, "cross",zoom=zoom,subSample=subSample, command=lambda event=None: UseCase.button_callback("cross"))
        self.cirle_button = ControllerButton(self, "circle",zoom=zoom,subSample=subSample, command=lambda event=None: UseCase.button_callback("circle"))

        self.addition_button.grid(row=0, column=1)
        self.triangle_button.grid(row=2, column=1)
        self.cross_button.grid(row=1, column=0)
        self.cirle_button.grid(row=1, column=2)