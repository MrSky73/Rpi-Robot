import customtkinter as ctk
import tkinter as tk

from presentation.view.commonWidget.ArrowButton import ArrowButton

class MovementButton(tk.Frame):
    def __init__(self, master, bg="white",**kwargs):
        super().__init__(master, bg="white",**kwargs)
            
        zoom =1
        subSample=1
        self.up_button = ArrowButton(self, "up",zoom=zoom,subSample=subSample)
        self.down_button = ArrowButton(self, "down",zoom=zoom,subSample=subSample)
        self.left_button = ArrowButton(self, "left",zoom=zoom,subSample=subSample)
        self.right_button = ArrowButton(self, "right",zoom=zoom,subSample=subSample)

        self.up_button.grid(row=0, column=1)
        self.down_button.grid(row=2, column=1)
        self.left_button.grid(row=1, column=0)
        self.right_button.grid(row=1, column=2)