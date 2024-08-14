import os

print(os.getcwd())

os.mkdir("newFolder")
print(os.listdir())
os.rmdir("newFolder")

print(os.getlogin())
print(os.system("whoami"))