import os
import shutil

import message as msg # defile shortcut of module
from message import bye   # got specific module

try:
    numerator = int(input("enter a number to devide: "))
    denominator = int(input("enter a number to devide by: "))
    result = numerator/denominator
    print(int(result))
except Exception as a:
    print("something went wrong :( ")    
    print(a)

# this open a file and close it automatically.
with open('test.txt') as dir:
    print(dir.read())


adding = "this  text is added from python exception_handling file"
with open('test.txt','a') as dir:
    dir.write(adding) 


    # shutil is also module which is good to work on multiple files.

# copyfile() = copies contents of a file
# copy()     = it includes copyfile() feature + permission mode + destination can be a directory.
#copy2()    = it contains copy() feature + copies metadata
    
shutil.copyfile('test.txt' , '../copy.txt')    


help("modules")