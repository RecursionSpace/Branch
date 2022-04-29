''' Graphic User Interface Launcher '''

from tkinter import ttk
from ttkthemes import ThemedTk

from modules import select_network

# class GuiLauncher(ttk.Frame):
#     def __init__(self, *args, **kwargs):
#         ttk.Frame.__init__(self, *args, **kwargs)
#         p1 = Page1(self)
#         p2 = Page2(self)
#         p3 = Page3(self)

#         buttonframe = ttk.Frame(self)
#         container = ttk.Frame(self)
#         buttonframe.pack(side="top", fill="x", expand=False)
#         container.pack(side="top", fill="both", expand=True)


def show_frame(cont):
    '''
    Shows the selected frame
    '''
    selected_frame = frames[cont]
    selected_frame.tkraise()


init_window = ThemedTk(theme="equilux")
init_window.attributes("-fullscreen", True)

# creating a container
container = ttk.Frame(init_window)
container.pack(side="top", fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

frames = {}

for F in (select_network.WiFiGUI,):
    frame = F(container, init_window)
    frames[F] = frame

    frame.grid(row=0, column=0, sticky="nsew")

show_frame(select_network.WiFiGUI(init_window))

# user_interface = select_network.WiFiGUI(init_window)

# user_interface.set_init_window()
# user_interface.scans_wifi_list()  # Scan for networks before starting

init_window.mainloop()
