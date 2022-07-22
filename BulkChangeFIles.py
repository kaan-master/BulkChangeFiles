import os
counter = 0
# change path after r
path = r"/mnt/c/Users/kaan/OneDrive/Documenten/demannen"
files = [] 
os.chdir(path)
for file_name in os.listdir (path):
    # input the place you want to change in the line under 
    replace = "Change this" 
    if  replace in file_name:
        old_name = file_name
        new_name = file_name.replace (replace, "")
        counter += 1
        files.append (new_name)
        os.rename (old_name, new_name)
print (counter)
print (files)