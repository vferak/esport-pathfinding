__author__ = "Lenka Skanderova"
__copyright__ = "(c)2020 VSB-TUO, FEECS, Dept. of Computer Science"
__email__ = "lenka.skanderova@vsb.cz"
__version__ = "0.1.0"


import tkinter as tk


class ToggleButton(tk.Button):
    """
    Toggle button
    """
    ON_config = {'relief': 'sunken'}
    OFF_config = {'relief': 'raised'}

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #self.image = PhotoImage(file=img_file)
        self.toggled = False
        self.config = self.OFF_config
        self.config_button()

        self.bind("<Button-1>", self.toggle)

    def toggle(self, *args):
        if self.toggled:
            self.config = self.OFF_config
        else:
            self.config = self.ON_config
        self.toggled = not self.toggled
        return self.config_button()

    def config_button(self):
        self['relief'] = self.config['relief']
        return "break"

    def __str__(self):
        return f"{self['relief']}"
