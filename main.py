#Assignment: Custom Automation
"""Automate some aspect of your life using Python.
Python automation ideas
https://medium.com/pythoneers/21-automation-ideas-for-2021-616313fd5e96
"""
"""
You've learnt about automation with Python and Selenium. 
It's your turn to get creative and automate some aspect of your life using what you have learnt.

This could be an aspect of your job, your schoolwork, your home, your chores. 
Think about your week and everything that you do on a regular basis, when do you feel like a robot? 
Which jobs do you find tedious and boring? 
Can it be automated?

Here are some stories for inspiration:
----------------------------------------------------------------------------------
Automate an email to your boss to ask for a raise every 3 months. =)
Automate your lights so they switch on when your phone is within the radius of your house.
Automatically organise the files in your downloads folder based on file type.
Automate your gym class bookings.
Automate your library book renewals.
Automate your job.
Automate your home chores.

Personally, I had a job in a hospital where I had to arrange all the doctors' shifts in my department (normal day, long day, night shift). 
It would depend on when they wanted to take annual leave/vacation and the staffing requirements. 
It started out in an Excel spreadsheet, by the time I was done with it, 
it was fully automated with Python and doctors were able to view a live version of the rota to see when they can take time off. 
The code took an evening to write and it saves me 3 hours per week. (More time to watch Netflix and eat ice cream).
Once you're done with the assignment, let us know what you automated in your life and maybe it will inspire another student!
"""
# Automatically organise the files in folder based on file type.
"""
1/Y. Open directory of folder (navigate to folder python: https://stackoverflow.com/questions/431684/equivalent-of-shell-cd-command-to-change-the-working-directory)
2/Y. Check all file names in directory for file types
    >>Detect all file types in folder python/ Detect file type python
    https://stackoverflow.com/questions/45256250/how-to-get-python-to-list-all-file-extensions-in-the-directories
    >>Remove duplicates from list
3/Y. Create directory for each file type 
    (Create folder python/Create folder in current directory if not exists)
    https://stackoverflow.com/questions/31008598/python-check-if-a-directory-exists-then-create-it-if-necessary-and-save-graph-t
4/Y. Move all files of certain file type to relevant directory 
    >> Move file python :https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
    
    
#IMPROVEMENTS;
Sort according to date instead of file name (parse the first few characters of file name to get the date)
"""
import os
from os import path

file_types = 0
file_type_list = []

# Open directory of folder
# os.chdir('C:/Users/Chua/Desktop/#STREETSOFNEWCAPENNA #ART')

#Check all file names in directory for file types (How to check current directory only and not all folders in directory for file type?)
# https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
ListFiles = os.listdir(os.getcwd())
print(f"ListFiles: {ListFiles}")
file_ext = []
for item in ListFiles:
   file_ext.append(item.split(".")[-1])
print(file_ext)

# ListFiles = os.walk(os.getcwd())
# print(ListFiles)
# SplitTypes = []
# for walk_output in ListFiles:
#     print("walk_output")
#     print(walk_output)
#     for file_name in walk_output[-1]:
#         SplitTypes.append(file_name.split(".")[-1])
# print(SplitTypes)

#Remove duplicate file types & creating directories for each file type
for item in file_ext:
    if item not in file_type_list:
        file_type_list.append(item)
print(file_type_list)

#Create directory for each file type
for item in file_type_list:
    if not os.path.exists(item):
        os.mkdir(item)

import shutil
# Move all files of certain file type to relevant directory
for i in range(len(ListFiles)):
    if "." in ListFiles[i]:
        print(ListFiles[i])
        if "main" not in ListFiles[i] and "idea" not in ListFiles[i]:
            shutil.move(f"{ListFiles[i]}", f"{ListFiles[i].split('.')[-1]}/{ListFiles[i]}")