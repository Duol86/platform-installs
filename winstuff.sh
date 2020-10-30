Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

iex ((New-Object System.Net.Webclient).DownloadString('https://git.io/debloat'))

choco install spotify powertoys protonvpn tor notepadplusplus vlc minecraft steam chromium obs git gimp

choco install kdenlive

choco install jre8
