ext = input("Type the file extention: ").lower().strip()

if not ext.startswith("."):
    ext = "."+ext
ext_list=[".txt",".log",".csv",".xlsx",".jpg",".png"]

for item in ext_list:
    if(item == ext):
        print("this will process" +  ext)