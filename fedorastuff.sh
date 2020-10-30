sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

sudo dnf install obs-studio -y

sudo dnf install xorg-xll-drv-nvidia-cuda -y

sudo dnf install spotify vlc steam gimp lutris chromium git -y

sudo dnf install -y openvpn dialog python3-pip python3-setuptools

sudo pip3 install protonvpn-cli

sudo dnf install gnome-software -y

sudo dnf install kdenlive -y

sudo dnf install wine-stable -y

sudo dnf install wget -y

wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9/npp.7.9.Installer.exe

wine npp.7.9.Installer.exe

su -c "yum install java-1.8.0-openjdk"
