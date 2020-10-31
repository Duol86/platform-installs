#!/usr/bin/python

print("Welcome to the platform-installs scripts")

import os
os.system("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")

print("Using this tool, you can debloat your windows installation. Edit the white/blacklist to change what is removed.
iex ((New-Object System.Net.Webclient).DownloadString('https://git.io/debloat'))

os.system("choco install spotify powertoys protonvpn tor notepadplusplus vlc minecraft steam chromium obs git gimp kdenlive jre8")
