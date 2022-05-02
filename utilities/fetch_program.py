''' Fetches a program from proved URL and run the installer. '''

import os


def clone(url):
    ''' Clones the repository from the given URL. '''
    os.chdir('/opt/')
    os.system(f'git clone {url}')
