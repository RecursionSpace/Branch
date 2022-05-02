''' Manages the implementation of SSH keys for the user. '''


from re import sub


def new_deploy_key():
    '''
    Creates a new key pair that is used for deployments.
    '''
    import os
    import subprocess
    import sys
    from pathlib import Path

    import ssh_agent_setup

    # Check if the key pair already exists.
    if Path('/home/{}/.ssh/id_rsa.pub'.format(os.environ['USER'])).is_file():
        print('The key pair already exists. Please remove it before creating a new one.')
        sys.exit(1)

    # Create the key pair.
    subprocess.call(['touch', '~/.ssh/id_rsa'], shell=True)
    subprocess.call(['touch', '~/.ssh/id_rsa.pub'], shell=True)
    subprocess.call(['ssh-keygen', '-t', 'ed25519', '-C',
                    f'{os.environ["USER"]}', '-f', '~/.ssh/id_rsa', '-q', '-N', '""'])
    subprocess.call(['chmod', '600', '~/.ssh/id_rsa'])
    subprocess.call(['chmod', '644', '~/.ssh/id_rsa.pub'])

    # Start the ssh-agent.
    # subprocess.call(['eval', '$(ssh-agent -s)'])
    ssh_agent_setup.setup()

    # Add your SSH private key to the ssh-agent.
    # subprocess.call(['ssh-add', '~/.ssh/id_rsa'])
    ssh_agent_setup.add_key('~/.ssh/id_rsa')


new_deploy_key()
