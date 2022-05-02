''' Graphic User Interface Launcher '''

import json

from tkinter import ttk
from ttkthemes import ThemedTk

from .modules import select_network, end_screen, install_program

from utilities import network

with open('/opt/Branch/branch.json', 'r', encoding="utf-8") as json_file:
    branch_settings = json.load(json_file)


class GUI(ThemedTk):
    '''Initializes the GUI'''

    def __init__(self, *args, **kwargs):
        ThemedTk.__init__(self, *args, **kwargs)

        self.title("WiFi Selection")
        self.attributes("-fullscreen", True)
        self.set_theme("equilux")

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")

        container = ttk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (select_network.WiFiGUI, install_program.InstallProgram, end_screen.EndScreen):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        if not network.is_connected():
            self.show_frame("WiFiGUI")

        if not branch_settings['program_installed']:
            self.show_frame("InstallProgram")
        else:
            self.show_frame("EndScreen")

    def show_frame(self, cont):
        '''
        Shows the selected frame
        '''
        selected_frame = self.frames[cont]
        selected_frame.tkraise()


def start_gui():
    '''
    Called to open the GUI
    '''
    app = GUI()
    app.mainloop()


# Launch the GUI if this is the main file
if __name__ == "__main__":
    app = GUI()
    app.mainloop()
