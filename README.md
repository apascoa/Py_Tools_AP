# Py_Tools_AP


## How to Use

Importing:
```python
#-------------------------/ Import Py_Tools_AP by APascoa /-------------------------#
import requests
r = requests.get("https://raw.githubusercontent.com/apascoa/PY_Tools/main/main.py")
Temp = open('Py_Tools_AP.py', 'wb')
Temp.write(r.content)
Temp.close()
#----------------------------/ Py_Tools_AP by APascoa /-----------------------------#
```

Example code for testing:
```python
#----------------------------------/ Example Code /---------------------------------#
from Py_Tools_AP import test
test()
#----------------------------------/ Example Code /---------------------------------#
```

Remove the file from the folder:
```python
#-------------------------/ Remove Py_Tools_AP by APascoa /-------------------------#
import os
os.remove(Temp.name)
#----------------------------------/ END of Code /----------------------------------#
```
