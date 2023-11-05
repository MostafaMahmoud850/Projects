import os
# get the current directory
cwd = os.getcwd()
print("Current working directory is:", cwd)
# change the current directory
os.chdir("D:\python")
cwd = os.getcwd()
print("Current working directory is:", cwd)
# create new directory
os.mkdir("Mastering Python - تعلم بايثون")
# change the current directory to the directory created by me
os.chdir("D:\python\Mastering Python - تعلم بايثون")

# create 152 files  
start = 1
last = 153
number_of_file = 0

for i in range(start, last):
    number_of_file += 1
    with open(f"{number_of_file}.py", "w") as f:
        f.write(f"# this file is number {i} in mastering python course from elzero_web_school.")