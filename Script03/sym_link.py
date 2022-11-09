#!/usr/bin/env python3
#Name: Muaz Osman
#Date: 11/09/2022

import os, subprocess
"""
TODO:
1 - Create the function that will create a symbolic link, we are expecting User to enter the file that they want to enter a short for
2 - Script checks to see if the file exits, and user is informed if it does not.
3 - The function that deletes the Symbolic link provided by the user
4 - the function that prints the summarized report of the links in the system
5 - the report has to be "User Friendly" aka easy to read and understand
6 - User is informed of their current working directory, i tihink its os.getcwd()
#Example of creating a SYMBLOIC LINK: 'ln -s /Users/name/Documents/MyFolder /Users/name/Desktop/MyFolder'
#Example of Removing a symbolic link: 'unlink <path-to-symlink>'
#How to find broken links: finding them -> 'find /home/james -xtype l' Deleteing them -> 'find /home/james -xtype l -delete'
"""

ShortCut = ""
Source = ""

def CreateLink():
    os.system('clear')
    #Get the UserName Linux.
    username = os.path.expanduser("~")
    #cd to the user's home directory
    os.chdir(username)
    #Get the Current Working Directory
    print("The Current Working Directory is:- {}".format(os.getcwd()))
    #the user is asked about the file name
    ShortCut = str(input("Enter the name of the shortcut: "))
    #the user is asked about the source file name
    Source = str(input("Enter the name of the source file: "))
    #Find if the files exists in the system
    if(os.path.exists(Source)):
        #Create the symbolic link
        try:
            os.symlink(Source, ShortCut)
            print("The Symbolic Link has been created")
        except:
            print("ERROR: The Symbolic Link could not be created!")
    else:
        print("ERROR: The file does not exist!")

def DeleteLink():
    os.system('clear')
    #Get the Current Working Directory
    print("The Current Working Directory is:- {}".format(os.getcwd()))
    #Get the UserName Linux
    username = os.path.expanduser("~")
    #cd to the user's home directory
    os.chdir(username)
    #the user is asked about the file name
    ShortCut = str(input("Enter the name of the shortcut: "))
    #Find if the files exists in the system
    if(os.path.exists(ShortCut)):
        #Deletes the symbolic link
        try:
            subprocess.Popen("unlink {}".format(ShortCut), shell=True, stdout=subprocess.PIPE).stdout.read()
            print("The Symbolic Link has been deleted")
        except:
            print("ERROR: The Symbolic Link could not be deleted!")
    else:
        print("ERROR: The file does not exist!")

def SummarizedReport():
    #Clearing the Terminal
    os.system('clear')
    #Get the UserName Linux
    username = os.path.expanduser("~")
    #cd to the user's home directory
    os.chdir(username)
    #Get the Current Working Directory
    print("The Current Working Directory is:- {}".format(os.getcwd()))
    #The summary report lists the symbolic links in the user’s home directory and prints them in a user-friendly format
    Links = subprocess.Popen("find . -type l", shell=True, stdout=subprocess.PIPE).stdout.read()
    #Filter the output so it is more User Friendly
    Links = Links.decode("utf-8")
    print("\nThe Symbolic Links in the user’s home directory are:- ")
    print(Links)
    #The summary report shows the number of links in the user’s home directory.
    NumberOfLinks = subprocess.Popen("find . -type l | wc -l", shell=True, stdout=subprocess.PIPE).stdout.read()
    #Filtering the output so it is more User Friendly
    NumberOfLinks = NumberOfLinks.decode("utf-8")
    print("The number of links in the user’s home directory is: ")
    #Printing the number of links
    print(NumberOfLinks)
    #The summary report shows the target path for each link.
    TargetPath = subprocess.Popen("find . -type l -exec readlink -f {} \;", shell=True, stdout=subprocess.PIPE).stdout.read()
    #Filtering the output so it is more User Friendly
    TargetPath = TargetPath.decode("utf-8")
    #Printing the output
    print("The target path for each link is: ")
    print(TargetPath)
    os.system('sleep 5')
    
#Clearing the terminal upon execution
os.system('clear')
def main():
    LoopTerminator = -1
    while(LoopTerminator != 0):
        while True:
            try:
                print("\n********************************************\n***** Welcome To Symolbic Link Manager *****\n********************************************\n")
                print("[1] Create a Symbolic Link")
                print("[2] Delete a Symbolic Link")
                print("[3] Summarized Report")
                print("[quit] Exit\n")
                #Strip just incase the user enters a space after the number
                UserInput = str(input("Enter your choice: ")).strip().lower()
                if(UserInput == "1"):
                    CreateLink()
                elif(UserInput == "2"):
                    DeleteLink()
                elif(UserInput == "3"):
                    SummarizedReport()
                elif(UserInput == "quit"):
                    os.system('clear')
                    print("\n*****************************************************\n***** Thank You For Using Symolbic Link Manager *****\n*****************************************************\n")
                    print("Quitting the Program in 3 Seconds...")
                    os.system('sleep 3')
                    LoopTerminator = 0
                    break
                else:
                    print("Invalid Input! Please Try Again!")
            except:
                #Expected Errors in the program
                print("Invalid Input! Please Try Again!")
                continue

main()