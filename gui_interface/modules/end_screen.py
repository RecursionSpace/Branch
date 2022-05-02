''' Final screen that is shown. '''

import json

from tkinter import ttk

from utilities import network


class EndScreen(ttk.Frame):
    '''Final Screen Elements'''

    def __init__(self, main_window, controller):
        ttk.Frame.__init__(self, main_window)
        self.main_window = main_window
        self.controller = controller

        label = ttk.Label(
            self, text=f"IP: {network.get_addresses()}",
            font=("Helvetica", 32)
        )
        label.pack(ipadx=20, ipady=20)

        try:
            with open('/opt/Branch/branch.json', 'r+', encoding="utf-8") as json_file:
                branch_settings = json.load(json_file)

            program_label = ttk.Label(
                self, text=f"Program: {branch_settings['program_name']}",
                font=("Helvetica", 32)
            )
            program_label.pack(ipadx=20, ipady=20)
        except KeyError as err:
            print(f"Could not open {err}")
            self.controller.show_frame("InstallProgram")

    def refresh(self):
        '''Resets the frame'''
        try:
            with open('/opt/Branch/branch.json', 'r+', encoding="utf-8") as json_file:
                branch_settings = json.load(json_file)

            program_label = ttk.Label(
                self, text=f"Program: {branch_settings['program_name']}",
                font=("Helvetica", 32)
            )
            program_label.pack(ipadx=20, ipady=20)
        except KeyError as err:
            print(f"Could not open {err}")
            self.controller.show_frame("InstallProgram")
