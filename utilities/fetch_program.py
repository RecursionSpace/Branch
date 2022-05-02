''' Fetches a program from proved URL and run the installer. '''

from git import Repo


def clone(url):
    ''' Clones the repository from the given URL. '''
    Repo.clone_from(url, '/opt')
