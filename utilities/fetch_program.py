''' Fetches a program from proved URL and run the installer. '''

import os
import json


def clone(url):
    ''' Clones the repository from the given URL. '''
    os.chdir('/opt/')
    os.system(f'git clone {url}')

    with open('/opt/Stem/stem.json', 'r+', encoding="utf-8") as json_file:
        branch_settings = json.load(json_file)

    branch_settings['branch_installed'] = True

    repo_name = url.split('/')[-1].split('.')[0]

    branch_settings['branch']['name'] = repo_name

    with open('/opt/Stem/stem.json', 'w', encoding="utf-8") as json_file:
        json.dump(branch_settings, json_file)

    return True
