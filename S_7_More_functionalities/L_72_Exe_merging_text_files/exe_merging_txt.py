import glob2
import datetime

# print(glob2.glob("*.txt"))

files = glob2.glob("file*")

def append_to_file(filename,toAppend):
    with open(filename,'a') as file:
        file.write(toAppend)

def copy_from_file(filename):
    with open(filename,"r") as file:
        x = file.read()
        return x

now = datetime.datetime.now()

for i in files:
    x = copy_from_file(i)
    append_to_file(now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", x + "\n")
