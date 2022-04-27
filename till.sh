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

# ---------------------------- Install Python 3.10 --------------------------- #
sudo apt install software-properties-common -y
yes '' | sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get --reinstall install python3.10 -y
