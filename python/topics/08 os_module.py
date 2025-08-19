import os
import pathlib

path = pathlib.Path("test_file.py")

# os.rename(path, "demo.py")
# os.mkdir("./OS_MKDIR")
# os.makedirs("./python_prc/decorators")  this is like mkdir -P
# os.remove("./demo.py")
# os.rmdir("./python_prc/decorators")
# os.removedirs("./python_prc/decorators")
# status = os.stat("./07 hashlib.py")

# print(status)

current_dir = os.getcwd()

split = os.path.split(current_dir)
parent_DIr = os.path.dirname(current_dir)
baseDir = os.path.basename(current_dir)

# print(parent_DIr)

folders = os.listdir()

print(folders)

# excercise : try to file rc files using python code

