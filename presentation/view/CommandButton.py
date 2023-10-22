class CommandButtons(tk.Frame):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback
        self.create_command_buttons()

    def create_command_buttons(self):
        # ... (similar logic as before)