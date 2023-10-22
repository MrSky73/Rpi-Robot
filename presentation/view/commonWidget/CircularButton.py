class CircularButtons(tk.Frame):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback
        self.create_circular_buttons()

    def create_circular_buttons(self, button_name, width, height, relx, rely, button_colour, border_colour):
        canvas_b = tk.Canvas(self.root, width=width, height=height, bg=button_colour, highlightthickness=0)
        canvas_b.place(relx=relx, y=rely)
        circle_b = canvas_b.create_oval(5, 5, 45, 45, fill=button_colour)
        canvas_b.tag_bind(circle_b, "<Button-1>", lambda e: self.button_callback(button_name))
