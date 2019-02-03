#!/usr/bin/env python3

# layonthehorn

import sys, re, os

if len(sys.argv) < 3:
    print("""Usage: {0} FILEPATH FILEEXTENSION""".format(sys.argv[0]))
    sys.exit(0)

# Saves the users path to search
filepath = sys.argv[1]
# Saves the regular expression to search by
searchpat = sys.argv[2]
# compiles the users regex for faster searching
searchreg = re.compile(r"{0}$".format(searchpat))
# creates an empty list to store the matched files
filelist = []
# holds the absolute file paths
dirlist = []

# this searches through the file path supplied
for direct, dirname, files in os.walk(filepath):
# Goes through the list of files in a directory
    for mfile in files:
# checks if any files match the regular expression
        if searchreg.search(mfile):
# joins the file name to the directory it's in for deletion later
            dirlist.append(os.path.join(direct,mfile))
            filelist.append(mfile)

# checks that some thing has been found
if len(filelist) != 0 and len(dirlist) != 0:

# zip allows me to iterate through two lists at once
    for refile, directory in zip(filelist, dirlist):
        userinput = input("Remove {0}? (y\\n) ".format(refile))
        if userinput.lower() == "y":
# attempts to delete the file
            try:
                os.remove(directory)
                print("File deleted")
# if deletion fails prints out an error message and file name
            except OSError as e:
                print("Error: {0} - {1}".format(e.filename, e.sterror))
else:
# if no matches were found reports it to user
    print("No matches found with {0}.".format(searchpat))
    
