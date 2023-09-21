class AppWithCustomShapes:
    def __init__(self, root):
        # Setting the main window properties
        self.root = root
        self.root.title("PiApp")
        self.root.geometry("1024x600")
        self.root.configure(bg="white")

        # Creating buttons
        self.create_movement_buttons()
        self.create_command_buttons()
        self.create_settings_button()

    def button_callback(self, button_name):
        print(f"{button_name} button pressed")

    def create_movement_buttons(self):
        arrow_size = 50
        x_offset = 10
        y_offset = 525 - arrow_size  # Placing it slightly above the very bottom

        # Left Arrow
        left_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        left_canvas.place(x=x_offset, y=y_offset)
        left_canvas.create_polygon(arrow_size, arrow_size/2, 0, 0, 0, arrow_size, fill="gray")
        left_canvas.bind("<Button-1>", lambda e: self.button_callback("left"))

        # Right Arrow
        right_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        right_canvas.place(x=x_offset + 2*arrow_size, y=y_offset)
        right_canvas.create_polygon(0, arrow_size/2, arrow_size, 0, arrow_size, arrow_size, fill="gray")
        right_canvas.bind("<Button-1>", lambda e: self.button_callback("right"))

        # Up Arrow
        up_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        up_canvas.place(x=x_offset + arrow_size, y=y_offset - arrow_size)
        up_canvas.create_polygon(arrow_size/2, 0, 0, arrow_size, arrow_size, arrow_size, fill="gray")
        up_canvas.bind("<Button-1>", lambda e: self.button_callback("up"))

        # Down Arrow
        down_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        down_canvas.place(x=x_offset + arrow_size, y=y_offset + arrow_size)
        down_canvas.create_polygon(arrow_size/2, arrow_size, 0, 0, arrow_size, 0, fill="gray")
        down_canvas.bind("<Button-1>", lambda e: self.button_callback("down"))

    def create_command_buttons(self):
        # A button (Horizontal Rectangular)
        btn_a = tk.Button(self.root, text="A", width=20, height=2,
                          command=lambda: self.button_callback("a"))
        btn_a.place(x=900, y=540 - btn_a.winfo_reqheight())

        # B button (Circular)
        canvas_b = tk.Canvas(self.root, width=50, height=50, bg="white", highlightthickness=0)
        canvas_b.place(x=950, y=480)
        circle_b = canvas_b.create_oval(5, 5, 45, 45, fill="gray")
        canvas_b.tag_bind(circle_b, "<Button-1>", lambda e: self.button_callback("b"))

        # C button (Vertical Rectangular)
        btn_c = tk.Button(self.root, text="C", width=4, height=5,
                          command=lambda: self.button_callback("c"))
        btn_c.place(x=1000, y=500)

    def create_settings_button(self):
        icon = PhotoImage(file="assets/settings_icon.png")
        btn = tk.Button(self.root, image=icon, command=lambda: self.button_callback("settings"))
        btn.image = icon
        btn.place(relx=1.0, y=10, anchor="ne")

# This block is for demonstration purposes. In actual implementation, you'll use the "if __name__ == '__main__':" block
root = tk.Tk()
app = AppWithCustomShapes(root)
root.mainloop()