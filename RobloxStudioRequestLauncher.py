import os
from urllib.request import urlopen
with urlopen("http://setup.roblox.com/versionQTStudio") as response:
    body = response.read()

print(os.getcwd())

os.chdir("/Program Files (x86)/Roblox/Versions")
os.chdir(body)
print(os.getcwd())
os.system("RobloxStudioBeta.exe")
