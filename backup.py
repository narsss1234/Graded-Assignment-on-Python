# import all the dependencies
import shutil
from datetime import date
import os
import sys

# Change the directory
os.chdir(sys.path[0])

# request for the file that needs a backup
filename = input("Please enter the file name that you want to create a backup for: ")

# def function to perform the back of the files and folders.
def take_backup(src_file_name, dst_file_name=None,src_dir='',dst_dir=''):

    try:

        # Extract the today's date
        today = date.today()
        date_format = today.strftime("%d_%b_%Y")

        # Make the source directory, where we wanna backup our files
        src_dir = src_dir + src_file_name

        # if user does not provide the source file, then throw a message...
        if not src_file_name:
            print("Please provide the source file name.")
            exit()
        
        try:
            
            # If user provides all the inputs
            if src_file_name and dst_file_name and src_dir and dst_dir:
                src_dir = src_dir+src_file_name
                dst_dir = dst_dir+dst_file_name

            # When user provides  None or empty string
            elif dst_file_name is None or not dst_file_name:
                dst_file_name = src_file_name
                dst_dir = dst_dir+date_format+dst_file_name

            # When user provides one or more space
            elif dst_file_name.isspace():
                dst_file_name = src_file_name
                dst_dir = dst_dir+date_format+dst_file_name

            # When user gives name for the backup copy
            else:
                dst_dir = dst_dir+date_format+dst_file_name

            # Copy files from source to dest, using shutil, and copy2 method
            shutil.copy2(src_dir, dst_dir)

            print("Backup Successful!")
        
        # Exception handling if the file is not found
        except FileNotFoundError:
            print("File does not exists!\n")
            print("Please give the complete path")

    # Exception handling when the given name is a folder
    except PermissionError:
        dst_dir = dst_dir+date_format+dst_file_name

        # Copy the entire folder from source to destination
        shutil.copytree(src_file_name, dst_dir)
        print("Backup for the folder is Successful!")

# call the backup function.
take_backup(filename)