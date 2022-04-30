''' Graphic User Interface Launcher '''

from tkinter import ttk
from ttkthemes import ThemedTk

from modules import select_network, end_screen


def show_frame(cont):
    '''
    Shows the selected frame
    '''
    selected_frame = frames[cont]
    selected_frame.tkraise()


init_window = ThemedTk(theme="equilux")
init_window.attributes("-fullscreen", True)

init_window.title("WiFi Selection")

width = init_window.winfo_screenwidth()
height = init_window.winfo_screenheight()
init_window.geometry(f"{width}x{height}")

# creating a container
container = ttk.Frame(init_window)
# container.pack(side="top", fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

frames = {}

for F in (select_network.WiFiGUI, end_screen.EndScreen):
    frame = F(container)
    frames[F] = frame

    frame.grid(row=0, column=0, sticky="nsew")

# show_frame(select_network.WiFiGUI)
show_frame(end_screen.EndScreen)

# user_interface = select_network.WiFiGUI(init_window)

# user_interface.set_init_window()
# user_interface.scans_wifi_list()  # Scan for networks before starting

init_window.mainloop()
