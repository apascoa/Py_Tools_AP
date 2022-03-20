#Work By APascoa
#https://github.com/apascoa/

#Imports
import subprocess
import sys
import os
import requests


#Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#test
def test():
    print("Working")

#Square_title
def square_title(text):
    largura = len(text)+4
    print("┏",(largura-2)*"-","┓\n| ",text," |\n┗",(largura-2)*"-","┛", sep="")

#Underline
def underline(text):
    print(len(text)*"-")

#Install pip module
def pip_install(packge):
    subprocess.check_call([sys.executable, "-m", "pip", "install", packge])

#Uninstall pip module
def pip_uninstall(packge):
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", packge])


#Clear Console
def clearConsole():
    command = 'cls' if os.name in ('nt', 'dos')  else "clear"
    os.system(command) 

#Import File from URL
def file_import(url,location="./"):
    url_reverse = url[::-1]
    filename_reverse = url_reverse.split("/")[0]
    filename = filename_reverse[::-1]
    filename = filename.split("?")[0]
    r = requests.get(url)
    Temp = open("%s%s" %(location,filename), 'wb')
    Temp.write(r.content)
    Temp.close()
    return filename

def test_import(packge,packge_install=""):
    packge_install = packge if packge_install == "" else packge_install
    try:
        __import__(packge)
    except Exception:
        print(bcolors.WARNING+"Python Module '%s' Not Instaled"%(packge)+bcolors.ENDC)
        subprocess.check_call([sys.executable, "-m", "pip", "install", packge_install])
    globals()[packge] = __import__(packge)
    if packge not in sys.modules:
        print(bcolors.WARNING+"Python Module '%s' Failed to Import"%(packge)+bcolors.ENDC)
        print(bcolors.WARNING+"Exiting"+bcolors.ENDC)
        quit()
    else:        
        print(bcolors.OKCYAN+"Python Module '%s' Imported Successfully"%(packge)+bcolors.ENDC)
