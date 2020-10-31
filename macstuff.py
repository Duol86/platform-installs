#!/usr/bin/python

print("Welcome to the platform-install scripts")

import os
os.system("/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"")
os.system("brew cask install spotify vlc steam obs gimp minecraft chromium protonvpn wine-stable")
os.system("brew install git wget")
os.system("wget https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v7.9/npp.7.9.Installer.exe")
os.system("wine npp.7.9.Installer.exe")
os.system("curl -O https://distfiles.macports.org/MacPorts/MacPorts-2.6.3.tar.bz2")
os.system("tar xf MacPorts-2.6.3.tar.bz2")
os.system("cd MacPorts-2.6.3/")
os.system("./configure")
os.system("make")
os.system("sudo make install")
os.system("cd")
os.system("sudo port install kdenlive")
os.system("wget https://javadl.oracle.com/webapps/download/AutoDL?BundleId=243728_61ae65e088624f5aaa0b1d2d801acb16")
os.system("./jre-8u271-macosx-x64.dmg")
