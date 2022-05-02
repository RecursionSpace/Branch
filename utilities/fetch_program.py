''' Fetches a program from proved URL and run the installer. '''

import os

from git import Repo


def clone(url):
    ''' Clones the repository from the given URL. '''
    remote_url = repo.remotes[0].config_reader.get(url)
    repo_name = os.path.splitext(os.path.basename(remote_url))[0]

    os.mkdir(f'/opt/{repo_name}')
    Repo.clone_from(url, f'/opt/{repo_name}')
