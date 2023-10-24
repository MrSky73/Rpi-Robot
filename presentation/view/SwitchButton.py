import tkinter as tk

from presentation.view.commonWidget.RectangularButton import RectangularButton

class SwitchButton(tk.Frame):
    def __init__(self, parent, callback=None,**kwargs):
        super().__init__(parent,**kwargs)
        self.button1 = RectangularButton(self, text="Switch to Gallery", command=callback)
        self.button1.pack(side=tk.LEFT, padx=5)