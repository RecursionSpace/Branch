# Branch

Prepares a device for the installation of custom software.

Branch is intended to be installed on devices that will be remotely located and running custom software. Branch handles the following functions through an installation guide:

- Network connection wizard (wifi, ethernet, bluetooth)
- Install from GitHub or URL

In addition to providing basic functionality, Branch lays out and enforces best practices for headless devices.

## Installation

During installation system packages are installed.

``` BASH
cd /opt/
git clone git@github.com:RecursionSpace/Branch.git
./till.sh
```

## Network Connection Wizard

The first step in the installation process is to connect the device to the network. The network connection wizard will guide the user through the process of connecting the device to the network.

### AP Mode

If supported, the device enters AP mode and broadcasts a network that the user can connect to. The user is then navigated to an interface that prompts the user to connect to an existing network or enter a new network.

### GUI Wizard

If a display is detected, the device will enter a GUI wizard that will guide the user through the process of connecting the device to the network.
