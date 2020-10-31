#!/usr/bin/python

import os
os.system("sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm")
os.system("sudo dnf install xorg-xll-drv-nvidia-cuda spotify vlc steam lutris gimp chromium git openvpn dialog python3-pip python3-setuptools gnome-software kdenlive wine-stable wget")
os.system("sudo pip3 install protonvpn-cli")
os.system("wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9/npp.7.9.Installer.exe")
os.system("wine npp.7.9.Installer.exe")
os.system("su -c "yum install java-1.8.0-openjdk"")
