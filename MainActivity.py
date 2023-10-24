import tkinter as tk
from tkinter import PhotoImage, filedialog
import customtkinter

from presentation.UseCase import UseCase
from presentation.view.CommandButton import CommandButton
from presentation.view.DisplayScreen import DisplayScreen
from presentation.view.MovementButton import MovementButton
from presentation.view.SettingButton import SettingButton
from presentation.view.SwitchButton import SwitchButton

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
        self.use_case = UseCase(self.root)

        # Creating widgets
        # self.movement_button = MovementButton(self.root)
        # self.movement_button.pack(pady=20)
        # self.movement = MovementButton(self.root)

        # self.command_button = CommandButton(self.root)
        # self.command_button.grid(row=0,column=1)

        self.settings_button = SettingButton(self.root)
        self.settings_button.pack(anchor="ne")

        # Camera or Image display
        self.display_screen = DisplayScreen(self.root)
        self.display_screen.pack(expand = True, fill= "both")

        # Switch between live camera and image gallery
        self.live_camera = False
        self.use_case = UseCase(self)
        self.switch_button = SwitchButton(self.root,callback=self.use_case.switch_display)
        self.switch_button.pack(anchor="center")

        # Initialize GPIO (mock code, uncomment and modify for actual use on Raspberry Pi)
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Assuming pin 17 for camera input

root = tk.Tk()
app = App(root)
root.mainloop()