''' User provides URL for the program to download and install. '''

from tkinter import ttk, StringVar

from utilities import fetch_program


class InstallProgram(ttk.Frame):
    ''' User provides URL for the program to download and install. '''

    def __init__(self, init_window_name, controller):
        ttk.Frame.__init__(self, init_window_name)
        self.controller = controller

        self.get_url_value = StringVar()  # URL Field

        label = ttk.Label(
            self, text="Enter the URL for the program to download and install:",
            font=("Helvetica", 16)
        )
        label.pack(ipadx=20, ipady=20)

        # URL Field
        url_entry = ttk.Entry(
            self, textvariable=self.get_url_value, width=50
        )
        url_entry.pack(ipadx=20, ipady=20)

        # URL Field
        button = ttk.Button(
            self, text="Install", command=self.install_program
        )
        button.pack(ipadx=20, ipady=20)

    def install_program(self):
        ''' Downloads and installs the program. '''
        url = self.get_url_value.get()
        if fetch_program.clone(url):
            self.controller.show_frame("EndScreen")

    def refresh(self):
        '''Resets the frame'''
        self.destroy()
        self.__init__()
