import os
import re
import shutil

steamPath = "D:\Programs\SteamCmd"
serverPackagesPath = ".\Packages"
scriptDir = os.path.dirname(os.path.abspath(__file__))

urls = input("Please enter the URLs of the workshop items you want to download (separated by comma):\n$ ").split(",")

print(urls)

ids = [] 

for url in urls:
    ids.append(re.sub("\D", "", url))

print(ids)

#for id in ids:
#    os.system(steamPath+"\steamcmd.exe +force_install_dir "+scriptDir+" +login anonymous +workshop_download_item 365960 "+id+" +quit")

rfcmpPath = ".\steamapps\workshop\content\\365960\\" 

for id in ids:
    for file in os.listdir(rfcmpPath+id+"\\"):
        print(file)
        shutil.move(rfcmpPath+id+"\\"+file, serverPackagesPath)



