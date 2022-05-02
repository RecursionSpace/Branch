''' Interface that displays available networks '''

import os
import time

from tkinter import (
    StringVar, W, NSEW, VERTICAL, NS, ttk, CENTER
)

import pywifi
from pywifi import const

if os.environ.get('DISPLAY', '') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')

#os.environ['DISPLAY'] = ':0'


class WiFiGUI(ttk.Frame):
    '''
    Creates the interface for the user to enter the WiFi network name and password.
    '''

    def __init__(self, init_window_name, controller):
        ttk.Frame.__init__(self, init_window_name)

        self.get_wifi_value = StringVar()  # SSID Field
        self.get_wifi_password_value = StringVar()  # Password Field

        self.wifi = pywifi.PyWiFi()  # Grab the NIC interface
        self.iface = self.wifi.interfaces()[0]  # Grab the first wireless card
        self.iface.disconnect()  # test link break all links
        time.sleep(1)  # sleep for 1 second

        # Test whether the network card is in a disconnected state
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

        # ----------------------------- List of Networks ----------------------------- #
        wifi_labelframe = ttk.LabelFrame(
            self, text="Available Networks"
            font=("Helvetica", 32)
        )

        wifi_labelframe.pack(fill="x", expand=True, ipadx=20, ipady=20)

        # Define tree structure and scroll bars
        self.wifi_tree = ttk.Treeview(
            wifi_labelframe, show="headings", columns=("a", "b", "d"))
        self.vbar = ttk.Scrollbar(wifi_labelframe,
                                  orient=VERTICAL, command=self.wifi_tree.yview)
        self.wifi_tree.configure(yscrollcommand=self.vbar.set)

        # Define tree structure and scroll bars
        self.wifi_tree.column("a", width=50, anchor="center")
        self.wifi_tree.column("b", width=100, anchor="center")
        self.wifi_tree.column("d", width=100, anchor="center")

        self.wifi_tree.heading("a", text="WiFi ID")
        self.wifi_tree.heading("b", text="SSID")
        self.wifi_tree.heading("d", text="Signal Strength")

        self.wifi_tree.grid(row=4, column=0, sticky=NSEW)
        self.wifi_tree.bind("<Double-1>", self.on_db_click)
        self.vbar.grid(row=4, column=1, sticky=NS)

        # ------------------------ Connect to Selected Network ----------------------- #
        labelframe = ttk.LabelFrame(
            self, width=400, height=200, text="Connect"
            font=("Helvetica", 32)
        )

        labelframe.pack(fill="x", expand=True)

        ttk.Button(labelframe, text="Re-Scan WiFi Networks",
                   command=self.scans_wifi_list).grid(column=0, row=0)

        ttk.Label(labelframe, text="Network Name:").grid(column=0, row=1)

        ttk.Entry(labelframe, width=12, textvariable=self.get_wifi_value).grid(
            column=1, row=1)

        ttk.Label(
            labelframe, text="WiFi Password:").grid(column=2, row=1)

        ttk.Entry(labelframe, width=10, textvariable=self.get_wifi_password_value).grid(
            column=3, row=1, sticky=W)

        ttk.Button(labelframe, text="Connect",
                   command=self.connect).grid(column=0, row=2)

        button = ttk.Button(self, text="Go to the end page",
                            command=lambda: controller.show_frame("EndScreen"))
        button.pack()

        self.scans_wifi_list()  # Scan for networks on launch

    def scans_wifi_list(self):
        '''
        Scan the surrounding wifi list
        '''
        print("Start scanning for nearby wifi networks...")
        self.iface.scan()
        time.sleep(1)
        scanres = self.iface.scan_results()

        print(f"Quantity: {len(scanres)}")

        self.show_scans_wifi_list(scanres)
        return scanres

    def show_scans_wifi_list(self, scans_res):
        '''
        show wifi list
        '''
        for index, wifi_info in enumerate(scans_res):
            self.wifi_tree.insert("", 'end', values=(
                index + 1, wifi_info.ssid, wifi_info.signal))

    def on_db_click(self, event):
        '''
        Treeview binding events. Updates network name to the selected network.
        '''
        self.sels = event.widget.selection()
        self.get_wifi_value.set(self.wifi_tree.item(self.sels, "values")[1])

    def connect(self):
        '''
        Connect to the wifi network
        '''
        wifi_ssid = str(self.get_wifi_value.get())
        pwd_Str = str(self.get_wifi_password_value.get())

        print(f"Connecting to {wifi_ssid} with password {pwd_Str}")

        self.profile = pywifi.Profile()
        self.profile.ssid = wifi_ssid  # wifi name
        self.profile.auth = const.AUTH_ALG_OPEN  # network card opening
        self.profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi encryption
        self.profile.cipher = const.CIPHER_TYPE_CCMP  # encryption unit
        self.profile.key = pwd_Str  # password
        self.iface.remove_all_network_profiles()  # delete all wifi files
        self.tmp_profile = self.iface.add_network_profile(self.profile)
        self.iface.connect(self.tmp_profile)  # Link
        time.sleep(5)

        # Working method to connect
        os.system(
            f"nmcli device wifi connect '{wifi_ssid}' password {pwd_Str}")

        return bool(self.iface.status() == const.IFACE_CONNECTED)
