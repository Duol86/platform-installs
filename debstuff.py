#!/usr/bin/python

print("Welcome to the platform-installs scripts")

import os
os.system("sudo apt install discord openvpn dialog python3-pip python3-setuptools git spotify vlc steam minecraft gimp chromium ffmpeg obs-studio gnome-software kdenlive wget openjdk-8-jre
os.system("sudo pip3 install protonvpn-cli")
os.system("echo "deb http://download.opensuse.org/repositories/home:/strycore/Debian_10/ ./" | sudo tee /etc/apt/sources.list.d/lutris.list")
os.system("wget -q https://download.opensuse.org/repositories/home:/strycore/Debian_10/Release.key -O- | sudo apt-key add -")
os.system("wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9/npp.7.9.Installer.exe")
os.system("wine npp.7.9.Installer.exe")
