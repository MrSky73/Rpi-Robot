class RectangularButtons(tk.Frame):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback
        self.create_rectangular_buttons()

    def create_rectangular_buttons(self, button_name, width, height, relx, rely):
        btn = tk.Button(self.root, text=button_name, width=width, height=height,command=lambda: self.button_callback(button_name))
        btn.place(relx=relx, y = rely, anchor="ne")
