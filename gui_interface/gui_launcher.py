''' Graphic User Interface Launcher '''

from ttkthemes import ThemedTk

from modules import select_network

init_window = ThemedTk(theme="equilux")
init_window.attributes("-fullscreen", True)

user_interface = select_network.WiFiGUI(init_window)

user_interface.set_init_window()
user_interface.scans_wifi_list()  # Scan for networks before starting

init_window.mainloop()
