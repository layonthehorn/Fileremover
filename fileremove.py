#!/usr/bin/env python3

# layonthehorn
import sys, re, os

def pickopmode(opmode):


    usagestatment ="""Usage: {0} cwd|abs searchpattern""".format(sys.argv[0]) 

# if the user select cwd then the program used their pwd
    if opmode.lower() == "cwd":
        try:
            while 1:
                addedpath = input("Enter an optional extra to your PWD.(Press enter for default) ")

# This checks that the user did not enter an absolute path
                if (re.search(r"^/",addedpath)):
                        print("Must be a relative path.")
                        continue

# if the user did not enter any addons it skips this code
                if addedpath != "":
                    userpwd = os.path.join(os.getcwd(),addedpath)
               
# This checks if the directory exists
                    if not os.path.isdir(userpwd):
                        print("That directory does not exist.")
                        continue
                    else:
                        break
                else:
                    userpwd = os.getcwd()
                    break

        except KeyboardInterrupt:
            print("\nOperation Canceled")
            sys.exit(0)
        
# if the user selected abs they must supply an absolute path
    elif opmode.lower() == "abs":
# asks the user for a path and checks that is is an absolute one 
# also checks if the file does actually exist
# continues the loop until both an absolute path is supplied and an existing path
        try:
            while 1:
        
                userpwd = input("Enter the absolute path. ")

                if not (re.search(r"^/",userpwd)):
                    print("Must be an absolute path")
                    continue

                if not (os.path.isdir(userpwd)):
                    print("Path does not exist.")
                    continue

                break
# This allows the user to cleanly cancel giving a path
        except KeyboardInterrupt:
            print("\nOperation Canceled")
            sys.exit(0)
        
    else:
        print(usagestatment)
        sys.exit(0)
#    print("userpwd",userpwd)
    return userpwd  
 


def findfiles(searchpat,userpwd):
#    print("userpwd",userpwd)
# compiles the users regex for faster searching
    searchreg = re.compile(r"{0}$".format(searchpat))
# creates an empty list to store the matched files
    filelist = []
# holds the absolute file paths
    dirlist = []

# this searches through the file path supplied
    for direct, dirname, files in os.walk(userpwd):
# Goes through the list of files in a directory
        for mfile in files:
# checks if any files match the regular expression
            if searchreg.search(mfile):
# joins the file name to the directory it's in for deletion later
                dirlist.append(os.path.join(direct,mfile))
                filelist.append(mfile)
#    print(filelist,dirlist)
    return (filelist,dirlist)



def filedeleter(filelist,dirlist,searchpat):
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


# if you are running this file directly this code will run.
# Otherwise if you are calling this file and using the functions in it
# inside another program this code is skipped.
if __name__ == "__main__":

# creating a usage statement for users
    usagestatment ="""Usage: {0} cwd|abs searchpattern""".format(sys.argv[0]) 

# checking if the user supplied the right number of arguments
    if len(sys.argv) < 3:
        print(usagestatment)
        sys.exit(0)

# Saves the users operation mode 
    sysopmode= sys.argv[1]
# saving the search pattern 
    syssearchpat = sys.argv[2]

# Takes the users op mode and figures out the working directory
    sysuserpwd = pickopmode(sysopmode)
    returnfiles = findfiles(syssearchpat,sysuserpwd)
    filedeleter(returnfiles[0],returnfiles[1],syssearchpat)


# ---- Notable imports used ----
#   os.walk() - Walks through the operating systems file path returning directories, files, and
#   directories names.
#   os.path.join() - Joins a directory path and a file name based on OS to form a absolute file path
#   os.path.isdir() - Checks if a supplied path exists and returns true or false.
#   os.getcwd() - Returns the users current working directory.
#   sys.argv[] - Is a list of arguments supplied on the command line.
#   sys.exit() - Will exit the program.
#   re.search() - Will search the whole supplied string for a match to a regular expression.
#   re.compile() - Compiles a regular expression for faster searching.
#   zip() - Allows the program to iterate through two lists at once.
#   
#
        
