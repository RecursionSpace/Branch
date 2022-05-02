''' Final screen that is shown. '''

from tkinter import ttk

from utilities import network


class EndScreen(ttk.Frame):
    '''Final Screen Elements'''

    def __init__(self, main_window, controller):
        ttk.Frame.__init__(self, main_window)
        self.main_window = main_window

        label = ttk.Label(
            self, text=f"IP: {network.get_addresses()}",
            font=("Helvetica", 14)
        )
        label.pack(ipadx=10, ipady=10)
