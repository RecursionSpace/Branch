'''Called to launch the branch program, determining how the user will interact with the program.'''

import os

from gui_interface import gui_launcher

# Launch the GUI if a display is detected
if bool(os.environ["DISPLAY"]):
    gui_launcher.start_gui()
