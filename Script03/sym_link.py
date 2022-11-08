import os, subprocess

"""
TODO:
1 - Create the function that will create a symbolic link, we are expecting User to enter the file that they want to enter a short for
2 - Script checks to see if the file exits, and user is informed if it does not.
3 - The function that deletes the Symbolic link provided by the user
4 - the function that prints the summarized report of the links in the system
5 - the report has to be "User Friendly" aka easy to read and understand
6 - User is informed of their current working directory, i tihink its os.getcwd()
"""
#Example of creating a SYMBLOIC LINK: 'ln -s /Users/name/Documents/MyFolder /Users/name/Desktop/MyFolder'
#Example of Removing a symbolic link: 'unlink <path-to-symlink>'
#How to find broken links: finding them -> 'find /home/james -xtype l' Deleteing them -> 'find /home/james -xtype l -delete'
def CreateLink(FileName, Destinantion, Source):
    pass

def DeleteLink(Filename,Destination,Source):
    pass

def SummarizedReport(FileName):
    pass

def main():
    LoopTerminator = -1
    while(LoopTerminator != 0):
        while True:
            try:
                print("Welcome to the Symbloic Link Script\n")
                print("[1] Create a Symbloic Link\n")
                print("[2] Delete a Link\n")
                print("[3] Symbolic Links Summarized Report\n")
                print("[quit] To Quit the Program\n")
                #Taking the input here
                Decision = str(input("Enter your selection: "))
            except:
                #Here is the exceptions to be added that we might face in the program running
                print("\nInvalid Input! Please Try again!")
                pass
            #Decision taking mechanism to call the functions upon selection
            if(Decision == "1"):
                CreateLink()
            if(Decision == "2"):
                DeleteLink()
            if(Decision == "3"):
                SummarizedReport()
            if(Decision == "quit" or Decision == "Quit"):
                LoopTerminator = 0

main()