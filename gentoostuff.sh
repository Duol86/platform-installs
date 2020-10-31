print("Welcome to the platform-installs scripts")

#My experience with gentoo is currently very limited. Please excuse me if I make any mistakes.

#This script is written in shell commands to make this script a bit easier to write

#wget
sudo emerge --ask net-misc/wget
#discord
sudo emerge --ask net-im/discord-bin
#steam
sudo emerge --ask --noreplace dev-vcs/git
wget -P /etc/portage/repos.conf/ https://raw.githubusercontent.com/anyc/steam-overlay/master/steam-overlay.conf
sudo maint sync --repo steam-overlay
sudo emerge --ask games-util/steam-launcher
#vlc
sudo emerge --ask media-video/vlc
#obs
sudo emerge --ask media-video/obs-studio
#gimp
sudo emerge --ask media-gfx/gimp
#chromium
sudo emerge --ask www-client/chromium
#git
sudo emerge --ask dev-vcs/git
#lutris
sudo emerge --ask games-util/lutris
#wine
sudo emerge --ask virtual/wine
#openvpn
sudo emerge -v net-vpn/openvpn
#python
sudo emerge --ask dev-lang/python:3.9
#dialog
sudo emerge --ask dev-util/dialog
#pip3
sudo emerge --ask dev-python/pip
#protonvpn
sudo pip3 install protonvpn-cli
#gnome-software
sudo emerge --ask gnome-extra/gnome-software
#Java
sudo emerge --ask virtual/jdk
#spotify
sudo emerge --ask media-sound/spotify
#notepad++
wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9/npp.7.9.Installer.exe
wine npp.7.9.Installer.exe
