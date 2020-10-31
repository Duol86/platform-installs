#!/usr/bin/python

print("Welcome to the platform-installs scripts!")

import os
os.system("sudo pacman -S discord vlc steam obs-studio gimp chromium git lutris wine-stable wget openvpn dialog python-pip python-setuptools flatpak gnome-software jre-openjdk")
os.system("yay -S kdenlive")
os.system("sudo pip3 install protonvpn-cli")
os.system("flatpak install spotify")
os.system("wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9/npp.7.9.Installer.exe")
os.system("wine npp.7.9.Installer.exe")
