#!/bin/bash

# ---------------------------------------------------------------------------- #
#                                   Installer                                  #
# ---------------------------------------------------------------------------- #

# ---------------------- Update Package List and Upgrade --------------------- #
sudo apt-get update -y && sudo apt-get upgrade -y

# ---------------------------- Update System Time ---------------------------- #
sudo timedatectl set-timezone UTC
sudo apt-get install chrony -y
sudo chronyd -q

# ------------------------- Install Bash Requirements ------------------------ #
sudo apt-get install jq -y
sudo apt-get install unzip -y
sudo apt-get install fastjar -y

# ---------------------------- Install Python 3.10 --------------------------- #
sudo apt install software-properties-common -y
yes '' | sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get --reinstall install python3.10 -y
sudo apt-get install python3-pip -y

sudo pip install ssh-agent-setup


# ----------------------- Install Dysplay Requirements ----------------------- #
sudo apt-get install -y x11-utils
sudo apt-get install xauth xorg -y
sudo apt-get install xorg openbox -y
sudo apt-get install xserver-xorg xinit -y
# sudo apt install ubuntu-desktop
# sudo apt install lightdm -y

# https://raspberrypi.stackexchange.com/questions/57128/how-to-boot-into-own-python-script-gui-only
sudo apt-get install nodm -y

# ------------------------- Create Configuration File ------------------------ #
sudo touch /opt/Branch/branch.json
echo '{
    "program_installed": false,
}' > /opt/Branch/branch.json


# -------------------------------- Setup User -------------------------------- #
sudo adduser --disabled-password --gecos "" branch
sudo usermod -aG sudo branch


sudo systemctl enable branch.service


# https://askubuntu.com/questions/193130/what-is-the-most-basic-window-manager-for-ubuntu-that-can-be-used-to-display-a-s
sudo apt-get install ratpoison -y
