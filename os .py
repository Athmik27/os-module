import os
import time

# cwd() and chdir() function
print(os.getcwd())

os.chdir("d:/GitWorkspace/")
print(os.getcwd())

# join() function
print(os.path.join("d:/GitWorkspace/", "py1.txt"))

# split() function
pathname = os.path.join("d:/GitWorkspace/", "py1.txt")
print(os.path.split(pathname))

# Get metadata of the file
print(os.stat("py1.txt"))

# Rename and remove
os.rename("py1.txt", "py2.txt")
os.remove("py2.txt")
