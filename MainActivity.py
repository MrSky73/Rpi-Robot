import tkinter as tk
from tkinter import PhotoImage, filedialog
import customtkinter
# Uncomment the next line when running on a Raspberry Pi
# import RPi.GPIO as GPIO

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):

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

        #Display
        # Camera or Image display
        self.display_canvas = tk.Canvas(self.root, width=640, height=480, bg="black")
        self.display_canvas.place(relx=0.5, rely=0.5, anchor="center")

        # Switch between live camera and image gallery
        self.switch_button = tk.Button(self.root, text="Switch to Gallery", command=self.switch_display)
        self.switch_button.place(x=400, y=10)

        self.live_camera = False

        # Initialize GPIO (mock code, uncomment and modify for actual use on Raspberry Pi)
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Assuming pin 17 for camera input

    def switch_display(self):
        if self.live_camera:
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
        self.live_camera = not self.live_camera
        
    def button_callback(self, button_name):
        print(f"{button_name} button pressed")

    def create_movement_buttons(self):
        arrow_size = 50
        x_offset = 10
        y_offset = 525 - arrow_size  # Placing it slightly above the very bottom

        # Left Arrow
        left_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        left_canvas.place(x=x_offset + 2*arrow_size, y=y_offset)        
        left_canvas.create_polygon(arrow_size, arrow_size/2, 0, 0, 0, arrow_size, fill="gray")
        left_canvas.bind("<Button-1>", lambda e: self.button_callback("right"))

        # Right Arrow
        right_canvas = tk.Canvas(self.root, width=arrow_size, height=arrow_size, bg="white", highlightthickness=0)
        right_canvas.place(x=x_offset, y=y_offset)
        right_canvas.create_polygon(0, arrow_size/2, arrow_size, 0, arrow_size, arrow_size, fill="gray")
        right_canvas.bind("<Button-1>", lambda e: self.button_callback("left"))

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
        btn_a.place(relx=0.8, y=600 - btn_a.winfo_reqheight())

        # B button (Circular)
        canvas_b = tk.Canvas(self.root, width=50, height=50, bg="white", highlightthickness=0)
        canvas_b.place(relx=0.85, y=500)
        circle_b = canvas_b.create_oval(5, 5, 45, 45, fill="gray")
        canvas_b.tag_bind(circle_b, "<Button-1>", lambda e: self.button_callback("b"))

        # C button (Vertical Rectangular)
        btn_c = tk.Button(self.root, text="C", width=4, height=5,
                          command=lambda: self.button_callback("c"))
        btn_c.place(relx=1, y = 500, anchor="ne")

    def create_settings_button(self):
        image = PhotoImage(file="assets/settings_icon.png")
        icon = image.zoom(5)
        icon = image.subsample(10)
        # icon = image.height(10)
        # icon = image.width(10)
        btn = tk.Button(self.root, image=icon, command=lambda: self.button_callback("settings"))
        btn.image = icon
        btn.place(relx=1.0, y=10, anchor="ne")

# This block is for demonstration purposes. In actual implementation, you'll use the "if __name__ == '__main__':" block
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App()
#     app.mainloop()
root = tk.Tk()
app = App(root)
root.mainloop()