from pathlib import Path
import os
import subprocess
import re,glob
import json
import sys

 # this is current folder
Path(r"c:\program files\Microsoft") # for windows use
Path("/usr/local/bin")
Path("python/01_variable.py")
set01 = Path()/"python"/"01_variable.py"

for item in Path().iterdir():
    isDir = item.is_dir()
    if (isDir):
        print(item)
        os.chdir(item)   # used for changing
        print(Path.cwd())
        tt =subprocess.getoutput("ls -lh") # it returns the output of running command 
        os.chdir("..")
        
        # print(f"tt {tt}")
      
        

Path.__str__()
