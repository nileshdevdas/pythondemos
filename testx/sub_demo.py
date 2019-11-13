import subprocess
import os


listofFiles = os.walk("c:/")
for l in listofFiles:
    print(l)
a = subprocess.run("notepad.exe")
print(a)