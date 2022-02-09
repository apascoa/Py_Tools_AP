#Work By APascoa
#https://github.com/apascoa/

#Imports
import subprocess
import sys

imports = ["requests"]

for packge in imports:
    try:
        __import__(packge)
    except Exception:
        print("Python Module '%s' Not Instaled"%(packge))
        subprocess.check_call([sys.executable, "-m", "pip", "install", packge])     
        
print("\n\n\nDependencies Installed Successfully")