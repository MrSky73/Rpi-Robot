import tkinter as tk
import customtkinter as ctk

class ArrowButton(tk.Canvas):
    def __init__(self, parent, direction="up", bg="black",arrow_size = 50, highlightthickness=0, command=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.arrow_direction = direction
        self.configure(command=command)
        self.draw_arrow(arrow_size)

    def draw_arrow(self,arrow_size):
        if self.arrow_direction == "up":
            self.create_polygon(arrow_size/2, 0, 0, arrow_size, arrow_size, arrow_size, fill="gray")
        elif self.arrow_direction == "down":
            self.create_polygon(arrow_size/2, arrow_size, 0, 0, arrow_size, 0, fill="gray")
        elif self.arrow_direction == "left":
            self.create_polygon(0, arrow_size/2, arrow_size, 0, arrow_size, arrow_size, fill="gray")
        elif self.arrow_direction == "right":
            self.create_polygon(arrow_size, arrow_size/2, 0, 0, 0, arrow_size, fill="gray")
