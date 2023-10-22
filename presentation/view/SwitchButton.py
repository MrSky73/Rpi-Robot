import tkinter as tk

from presentation.view.commonWidget.RectangularButton import RectangularButton

class SwitchButton(tk.Canvas):
    def __init__(self, parent, callback=None):
        super().__init__(parent)
        self.grid() 
        self.switch_button = RectangularButton(
            parent=self,
            button_name="Switch to Gallery",
            width=20,
            height=2
        )