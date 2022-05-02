''' Final screen that is shown. '''

from tkinter import ttk

import utilities


class EndScreen(ttk.Frame):
    '''Final Screen Elements'''

    def __init__(self, main_window, controller):
        ttk.Frame.__init__(self, main_window)
        self.main_window = main_window

        label = ttk.Label(self, text=utilities.network.get_addresses())
        label.pack(side="top", fill="x", expand=True)
