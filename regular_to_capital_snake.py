# Example File.txt > Example_File.txt

import os

folder_files = os.listdir()  # get list of files in working dir

for file in folder_files:  # go through each file
    if os.path.isfile(file):  # check if 'file' is a file (not folder)
        if not file == os.path.basename(__file__):  # check if 'file' is this script
            file_rename = file.replace(" ", "_")  # replace spaces with underscores

            os.rename(file, file_rename)  # rename the file
    else:
        continue
