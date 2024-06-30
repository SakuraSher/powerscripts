import os
import sys
import shutil

def movefiles(file,dir):
    try:
        shutil.copy2(src=file,dst=dir)
    except Exception as e:
        print(e)
    


if __name__ =="__main__":
    if len(sys.argv) < 2 :
        print("name of the files have not been supplied")
    movefiles(sys.argv[1],sys.argv[2])

