import tkinter as tk

from presentation.view.commonWidget.RectangularButton import RectangularButton

class SwitchButton(tk.Frame):
    def __init__(self, parent,text="Switch to Gallery", bg="white", command=None,**kwargs):
        super().__init__(parent,bg="white",**kwargs)
        self.button1 = RectangularButton(self, text="Switch to Gallery", command=command)
        self.button1.pack(side=tk.LEFT, padx=5)
    
    def set_text(self, text):
        self.button1.configure(text=text)