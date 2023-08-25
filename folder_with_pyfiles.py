import os
import shutil

# Create the folder
os.mkdir("Python_Scripts2")

# Get the number of files from the user
num_files = int(input("Enter the number of files to create: "))

# Create the files
for i in range(num_files):
    filename = f"file{i}.py"
    open(os.path.join("Python_Script", filename), "a").close()