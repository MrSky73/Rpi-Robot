import tkinter as tk
from presentation.view.commonWidget.CircularButton import CircularButtons
from presentation.view.commonWidget.RectangularButton import RectangularButton

class CommandButton(tk.Frame):
    def __init__(self, parent, callback=None):
        super().__init__(parent)

        # A button (Horizontal Rectangular)
        self.a_rectangular_button = RectangularButton(
            parent=self,
            button_name="A",
            width=20,
            height=2
        )

        # B button (Circular)
        self.b_circular_button = CircularButtons(
            parent=self,
            button_name="B",
            width=50,
            height=50,
            relx=0.85,
            rely=500,
            button_colour="gray",
            border_colour="black"
        )

        # C button (Vertical Rectangular)
        self.a_rectangular_button = RectangularButton(
            parent=self,
            button_name="C",
            width=20,
            height=2
        )