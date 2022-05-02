''' Fetches a program from proved URL and run the installer. '''

import os

from git import Repo


def clone(url):
    ''' Clones the repository from the given URL. '''
    repo = Repo(url)
    repo_name = repo.remotes.origin.url.split('.git')[0].split('/')[-1]
    print(f"Cloning {repo_name}...")

    os.mkdir(f'/opt/{repo_name}')
    Repo.clone_from(url, f'/opt/{repo_name}')
