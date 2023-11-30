import os
folder=os.listdir("data")
print(os.getcwd())
# print(os.chdir("/Users")) you can change the directory of a folder
print(folder)
for folders in folder:
    print(folders)
    print(os.listdir(f"data/{folders}"))