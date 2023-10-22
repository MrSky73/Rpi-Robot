class SettingsButton(tk.Frame):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback
        self.create_settings_button()

    def create_settings_button(self, relx, rely, icon_address, icon_name, zoom, subsample ):
        image = PhotoImage(file=icon_address)
        icon = image.zoom(zoom)
        icon = image.subsample(subsample)
        # icon = image.height(10)
        # icon = image.width(10)
        btn = tk.Button(self.root, image=icon, command=lambda: self.button_callback(icon_name))
        btn.image = icon
        btn.place(relx=relx, y=rely, anchor="ne")