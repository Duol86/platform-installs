#!/usr/bin/python

print("Welcome to the platform-install scripts")

import os
os.system("/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"")
os.system("brew install --cask spotify vlc steam obs gimp minecraft chromium protonvpn wine-stable")
os.system("brew install git wget")
os.system("wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9/npp.7.9.Installer.exe")
os.system("wine npp.7.9.Installer.exe")
os.system("wget https://javadl.oracle.com/webapps/download/AutoDL?BundleId=243728_61ae65e088624f5aaa0b1d2d801acb16")
os.system("./jre-8u271-macosx-x64.dmg")
