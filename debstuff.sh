sudo apt install -y openvpn dialog python3-pip python3-setuptools

sudo pip3 install protonvpn-cli

sudo apt install git spotify vlc steam minecraft gimp chromium -y

sudo apt install ffmpeg -y

sudo apt install obs-studio -y

sudo apt install gnome-software -y

echo "deb http://download.opensuse.org/repositories/home:/strycore/Debian_10/ ./" | sudo tee /etc/apt/sources.list.d/lutris.list

wget -q https://download.opensuse.org/repositories/home:/strycore/Debian_10/Release.key -O- | sudo apt-key add -

sudo apt update -y

sudo apt install lutris -y

sudo apt install wget -y

wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9/npp.7.9.Installer.exe

wine npp.7.9.Installer.exe
