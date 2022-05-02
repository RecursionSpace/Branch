''' Fetches a program from proved URL and run the installer. '''

import os
import json


def clone(url):
    ''' Clones the repository from the given URL. '''
    os.chdir('/opt/')
    os.system(f'git clone {url}')

    with open('/opt/Branch/branch.json', 'r+', encoding="utf-8") as json_file:
        branch_settings = json.load(json_file)

    branch_settings['program_installed'] = True

    repo_name = url.split('/')[-1].split('.')[0]

    branch_settings['program_name'] = repo_name

    with open('/opt/Branch/branch.json', 'w', encoding="utf-8") as json_file:
        json.dump(branch_settings, json_file)

    return True
