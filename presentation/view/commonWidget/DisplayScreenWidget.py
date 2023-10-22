import tkinter as tk

class DisplayScreenWidget(tk.Canvas):
    def __init__(self, parent, width=640, height=480, bg="black", relx =0.5, rely =0.5, anchor = "center",**kwargs,):
        super().__init__(parent, width=width, height=height, bg=bg, **kwargs)
        self.place(relx=relx, rely=rely, anchor=anchor)