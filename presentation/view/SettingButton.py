import tkinter as tk
from presentation.view.commonWidget.ImageButton import ImageButton

class SettingsButton(tk.Canvas):
    def __init__(self, parent, callback=None):
        super().__init__(parent)
        self.setting_button = ImageButton(
            parent=self,
            callback=callable,
            relx= 1.0,
            rely=10,
            icon_address="assets/settings_icon.png",
            icon_name="Setting",
            zoom=5,
            subsample=10
        )