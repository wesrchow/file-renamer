# file-renamer
This is a collection of Python scripts that converts other files in the working directory from a given naming case to another. You should be able
 to copy the script into any folder and run it to rename all the files there. The script that runs this and other folders in the directory are not
  renamed (folder renaming may be added later).
<br/>

#### Conversions Currently Supported
* **Snake Case to Regular Naming:** `example_file.txt > Example File.txt`
<br/>
* **Regular Naming to Capital Snake Case:** `Example File.txt > Example_File.txt`
<br/>

*Note for `snake_to_regular.py`: Words that are in all caps (`EXAMPLE_FILE.txt`) will be replaced with regular naming (`Example File.txt`) (This
 may be changed in the future to support acronyms)*
