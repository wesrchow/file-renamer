# example_file.txt > Example File.txt

# TODO: add folder renaming support, check for other exceptions, spaces in file extension checking, code other conversions for different naming
#  conventions

import os

folder_files = os.listdir()  # get list of files in working dir

for file in folder_files:  # go through each file
    if os.path.isfile(file):  # check if 'file' is a file (not folder)
        if not file == os.path.basename(__file__):  # check if 'file' is this script
            file_rename = file.replace("_", " ").title()  # replace underscores with spaces & capitalize first char of words
            file_rename = file_rename[:file_rename.rindex(".") + 1] + file_rename[
                file_rename.rindex(".") + 1].lower() + file_rename[file_rename.rindex(".") + 2:]  # set file extension back to lowercase

            os.rename(file, file_rename)  # rename the file
    else:
        continue
