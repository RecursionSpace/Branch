''' Final screen that is shown. '''

from tkinter import ttk


class EndScreen(ttk.Frame):
    '''Final Screen Elements'''

    def __init__(self, main_window):
        ttk.Frame.__init__(self, main_window)
        self.main_window = main_window

        label = ttk.Label(text="Page 2")
        label.pack(side="top", fill="x", expand=True)
