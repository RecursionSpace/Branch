''' Network utilities '''

import socket


def is_connected():
    '''
    Check if the system is networked
    '''
    return bool(get_addresses() != '127.0.0.1')


def get_addresses():
    '''
    Get the addresses of the network interfaces
    '''
    network_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    network_socket.settimeout(0)

    try:
        # doesn't even have to be reachable
        network_socket.connect(('10.255.255.255', 1))
        ip_address = network_socket.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        network_socket.close()

    return ip_address
