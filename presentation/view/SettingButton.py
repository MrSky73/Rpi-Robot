import tkinter as tk
from presentation.view.commonWidget.ImageButton import ImageButton

class SettingButton(tk.Frame):
    def __init__(self, parent, image_name= "Setting",bg="white", command=None, **kwargs):
        super().__init__(parent, bg="white",**kwargs)
        
        asset_path = f"./assets/settings_icon.png" 
        self.button = ImageButton(self, image_path=asset_path, zoom = 5, subSample = 50, command=command)
        self.button.pack(padx=5, pady=5)
