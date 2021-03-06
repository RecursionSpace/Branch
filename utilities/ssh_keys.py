''' Manages the implementation of SSH keys for the user. '''

import os
import subprocess
import sys
from pathlib import Path

import ssh_agent_setup


def new_deploy_key():
    '''
    Creates a new key pair that is used for deployments.
    '''

    # Check if the key pair already exists.
    if Path(f'/home/{os.environ["USER"]}/.ssh/id_rsa.pub').is_file():
        print('The key pair already exists. Please remove it before creating a new one.')
        sys.exit(1)

    # Create the key pair.
    subprocess.call([
        'ssh-keygen', '-t', 'ed25519',
        '-C', f'{os.environ["USER"]}',
        '-f', f'/home/{os.environ["USER"]}/.ssh/id_rsa',
        '-q', '-N', '""'
    ])

    subprocess.call(
        ['chmod', '600', f'/home/{os.environ["USER"]}/.ssh/id_rsa'])

    subprocess.call(
        ['chmod', '644', f'/home/{os.environ["USER"]}/.ssh/id_rsa.pub'])

    # Start the ssh-agent.
    # subprocess.call(['eval', '$(ssh-agent -s)'])
    ssh_agent_setup.setup()

    # Add your SSH private key to the ssh-agent.
    # subprocess.call(['ssh-add', '~/.ssh/id_rsa'])
    ssh_agent_setup.add_key(f'/home/{os.environ["USER"]}/.ssh/id_rsa')


new_deploy_key()
