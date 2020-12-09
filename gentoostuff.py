#!/usr/bin/python

print("Welcome to the platform-installs scripts")

#My experience with gentoo is currently very limited. Please excuse me if I make any mistakes.

import os

#wget
os.system("sudo emerge --ask net-misc/wget")
#discord
os.system("sudo emerge --ask net-im/discord-bin")
#steam
os.system("sudo emerge --ask --noreplace dev-vcs/git")
os.system("wget -P /etc/portage/repos.conf/ https://raw.githubusercontent.com/anyc/steam-overlay/master/steam-overlay.conf")
os.system("sudo maint sync --repo steam-overlay")
os.system("sudo emerge --ask games-util/steam-launcher")
#vlc
os.system("sudo emerge --ask media-video/vlc")
#obs
os.system("sudo emerge --ask media-video/obs-studio")
#gimp
os.system("sudo emerge --ask media-gfx/gimp")
#chromium
os.system("sudo emerge --ask www-client/chromium")
#git
os.system("sudo emerge --ask dev-vcs/git")
#lutris
os.system("sudo emerge --ask games-util/lutris")
#wine
os.system("sudo emerge --ask virtual/wine")
#openvpn
os.system("sudo emerge -v net-vpn/openvpn")
#python
os.system("sudo emerge --ask dev-lang/python:3.9")
#dialog
os.system("sudo emerge --ask dev-util/dialog")
#pip3
os.system("sudo emerge --ask dev-python/pip")
#protonvpn
os.system("sudo pip3 install protonvpn-cli")
#gnome-software
os.system("sudo emerge --ask gnome-extra/gnome-software")
#Java
os.system("sudo emerge --ask virtual/jdk")
#spotify
os.system("sudo emerge --ask media-sound/spotify")
#notepad++
os.system("wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9/npp.7.9.Installer.exe")
os.system("wine npp.7.9.Installer.exe")