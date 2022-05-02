'''Called to launch the branch program, determining how the user will interact with the program.'''
import os
import json

from gui_interface import gui_launcher

# Open branch.json or create it if it doesn't exist
# if not os.path.exists('/opt/Branch/branch.json'):
#     with open('/opt/Branch/branch.json', 'w', encoding="utf-8") as f:
#         branch_json = {
#             'program_installed': False,
#         }
#         data = json.loads(branch_json)
#         json.dump(data, f)

# with open('/opt/Branch/branch.json', 'r', encoding="utf-8") as json_file:
#     branch_settings = json.load(json_file)

# Launch the GUI if a display is detected
if bool(os.environ["DISPLAY"]):
    gui_launcher.start_gui()
