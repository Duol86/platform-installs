# platform-installs
platform-installs is a  colllection of scripts I can use for the three main platform (Linux, Windows, MacOS) to install "the essentials" for a computer.


the main packages installed are spotify, vlc, steam, obs, gimp, minecraft, chromium, git, Java runtime, notepad++ and protonvpn.
All the packages are installed with various package managers for different platforms.


The package managers used are: APT (Debain Linux), Pacman (Arch Linux), Yay (Arch Linux AUR), Flatpak (Linux), Chocolatey (Windows 7-10), Brew (MacOS).

Wget is also used for the np++ install and the macos java install.


You can run these scripts in Linux and MacOS by downloading the zip file of the repo or cloning the repository. on Windows 10 it is done via opening powershell as administrator and inputting this command: iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/JTSpF'))

# IMPORTANT
This is a script that I would not recommend people use, it is created mainly for me to test out new thing I have learned in python and expand my knowledge.

# Dependecies
XCODE COMMAND LINE TOOLS IS REQUIRED FOR MAC USERS RUNNING THIS SCRIPT*

PYTHON 3 IS REQUIRED FOR ALL USERS RUNNING THIS SCRIPT

*xcode command line tools will be installed automatically through the brew installation script

# Soon to come!
I am currently working on a gui for these scripts and hope to combine them all into one single script!

# Update Notes:
v3.2: Removed kdenlive (installed through macports) from macstuff.py (because it required a full xcode installation)

v3.1: Replaced gentoostuff.sh (shell) with gentoostuff.py (python)

v2.0: Changed the scripts to the python 3 programming language

v1.1: Added Java runtime and OpenJDK to the packages installed
