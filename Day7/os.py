import os

os.mkdir("Path")
cwd=os.getcwd()
print(cwd)
 
path="D:/"
dir_l=os.listdir(path)
print("Files and directories in '",path,"':")
print(dir_l)

os.rmdir("Path")












