import tkinter as tk

from presentation.view.commonWidget.DisplayScreenWidget import DisplayScreenWidget


class DisplayScreen(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.displayScreen = DisplayScreenWidget(
            parent=self,
            width=640,
            height=480,
            bg="black",
            relx=0.5,
            rely=0.5,
            anchor="center",
        )