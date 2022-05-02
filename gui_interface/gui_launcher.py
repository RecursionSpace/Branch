''' Graphic User Interface Launcher '''

from tkinter import ttk
from ttkthemes import ThemedTk

from .modules import select_network, end_screen


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
