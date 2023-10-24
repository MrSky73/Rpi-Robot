import tkinter as tk
from presentation.view.commonWidget.DisplayScreenWidget import DisplayScreenWidget

class DisplayScreen(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.display_widget = DisplayScreenWidget(self)
        self.display_widget.pack(expand=True, fill="both")
    
    def create_image(self, x, y, **kwargs):
        return self.display_widget.create_image(x, y, **kwargs)
