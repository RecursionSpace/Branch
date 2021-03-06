<div align="center">

# Branch

[![Code Quality](https://github.com/RecursionSpace/Branch/actions/workflows/pylint.yml/badge.svg)](https://github.com/RecursionSpace/Branch/actions/workflows/pylint.yml)

</div>

## Table of Contents

- [Branch](#branch)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Network Connection Wizard](#network-connection-wizard)
    - [AP Mode](#ap-mode)
    - [GUI Wizard](#gui-wizard)
  - [Configuration](#configuration)
  - [process](#process)
  - [Definitions](#definitions)

Prepares a device for the installation of custom software.

Branch is intended to be installed on devices that will be remotely located and running custom software. Branch handles the following functions through an installation guide:

- Network connection wizard (wifi, ethernet, bluetooth)
- Install from GitHub or URL

In addition to providing basic functionality, Branch lays out and enforces best practices for headless devices.

## Installation

During installation system packages are installed.

``` BASH
cd /opt/
git clone https://github.com/RecursionSpace/Branch.git
./till.sh
```

## Network Connection Wizard

The first step in the installation process is to connect the device to the network. The network connection wizard will guide the user through the process of connecting the device to the network.

### AP Mode

If supported, the device enters AP mode and broadcasts a network that the user can connect to. The user is then navigated to an interface that prompts the user to connect to an existing network or enter a new network.

### GUI Wizard

If a display is detected, the device will enter a GUI wizard that will guide the user through the process of connecting the device to the network.

https://superuser.com/questions/610084/putty-x11-proxy-wrong-authorisation-protocol-attempted

## Configuration

Branch can be configured via the branch.json file in the root of the branch directory.

```json
{
  "program": {
    "url": "",
    "branch": "",
    "name": "",
  },
}
```

## process

A new user is created that will auto login using lightdm

Create a desktop file *branch.desktop* under `/usr/share/xsessions`

```BASH
[Desktop Entry]
Name=Branch GUI
Comment=Start application on boot
Exec=/opt/Stem/gui_interface/gui.sh
Type=Application
```

Edit `/etc/lightdm/lightdm.conf`

```BASH
[SeatDefaults]
autologin-user=jmerrell
autologin-user-timeout=0
user-session=branch
```

https://stackoverflow.com/questions/34917237/make-git-clone-with-sudo

## Definitions

*Stem* - This program that allows for branch programs to connect to.
*Branch* - The program that is connected to the stem.
