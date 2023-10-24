from tkinter import filedialog
import tkinter as tk


class UseCase:
    def __init__(self, app):
        self.app = app

    # def button_callback(self,button_name):
    #     print(f"{button_name} button pressed")

    @staticmethod
    def button_callback(button_name):
        print(f"{button_name} button pressed")

    def switch_display(self):
        if self.app.live_camera:
            self.switch_button.config(text="Switch to Gallery")
            # Switch to image from gallery
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                self.image = tk.PhotoImage(file=file_path)
                self.display_canvas.create_image(320, 240, image=self.image)
        else:
            self.switch_button.config(text="Switch to Live Camera")
            # Mock code for displaying camera input, replace with actual camera input code
            self.display_canvas.create_rectangle(10, 10, 630, 470, fill="blue", outline="yellow", width=3)
        self.app.live_camera = not self.app.live_camera
        