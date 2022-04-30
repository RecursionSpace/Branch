''' Graphic User Interface Launcher '''

from tkinter import ttk
from ttkthemes import ThemedTk

from modules import select_network, end_screen


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

        for F in (select_network.WiFiGUI, end_screen.EndScreen):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WiFiGUI")

    def show_frame(self, cont):
        '''
        Shows the selected frame
        '''
        selected_frame = self.frames[cont]
        selected_frame.tkraise()


# init_window = ThemedTk(theme="equilux")
# init_window.attributes("-fullscreen", True)

# init_window.title("WiFi Selection")

# width = init_window.winfo_screenwidth()
# height = init_window.winfo_screenheight()
# init_window.geometry(f"{width}x{height}")

# creating a container
# container = ttk.Frame(init_window)
# container.pack(side="top", fill="both", expand=True)

# container.grid_rowconfigure(0, weight=1)
# container.grid_columnconfigure(0, weight=1)

# frames = {}

# for F in (select_network.WiFiGUI, end_screen.EndScreen):
#     frame = F(container)
#     frames[F] = frame

#     frame.grid(row=0, column=0, sticky="nsew")

# show_frame(select_network.WiFiGUI)
# show_frame(end_screen.EndScreen)

# user_interface = select_network.WiFiGUI(init_window)

# user_interface.set_init_window()
# user_interface.scans_wifi_list()  # Scan for networks before starting

if __name__ == "__main__":
    app = GUI()
    app.mainloop()

# init_window.mainloop()
