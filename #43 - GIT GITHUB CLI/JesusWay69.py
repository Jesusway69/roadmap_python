import os, platform, git


if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')




path = r"C:\Users\jesus\Documents\Python3project\GitProjectPython\\"
my_repo = git.repo(path)

