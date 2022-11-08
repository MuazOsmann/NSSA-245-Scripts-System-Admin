#!/usr/bin/env python3

#Name: Muaz Osman
#Date: 28/09/2022

#imports needed libraries for the script to work.
import os, subprocess, socket,time

"""   
        
        the script will test connectivity to the gateway, a remote IP address, and a URL to validate that DNS resolution is working
        Default Gateway -> PFSense (SHould be obtained Automatically {192.168.1.254})
        Remote IP Address -> RIT DNS {129.21.3.17}
        DNS Resolution -> www.google.com
                                                                                                                                        """

#the beginning of the script test, 
#Clear the Terminal
os.system('cls' if os.name == 'nt' else 'clear')

def DGWGetterAndTest(): #Default GateWay Grabbing and Testing Connectivity Function
    """
    This function will grab the default gateway of the device and test the connectivity to it when called.
    it will return the default gateway IP address if it is reachable and 0 if it is not reachable.
    """
    #Getting the Host name from the device
    MachineName = socket.gethostname()
    #Cleaning the Terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    #   Grabbing the IP Default Gateway
    #get the default gateway using the route command
    route = subprocess.Popen(["route"], stdout=subprocess.PIPE)
    #use grep to filter the output to only show the default gateway
    grep = subprocess.Popen(["grep", "default"], stdin=route.stdout, stdout=subprocess.PIPE)
    #print the output of the default gateway
    output = grep.communicate()[0]
    #Getting the IP Address of the Default Gateway
    DGWAddr= socket.gethostbyname(output.decode('utf-8').split()[1]) #DGWAddr = Default GateWay Address
    #Testing the Default Gateway address Connection.
    print("\n* The Default Gateway Address is:- {}\n".format(DGWAddr))
    #Collecting the Response from the Server
    Response = os.system("ping -c 4 " + DGWAddr)
    #Evaluating the Response
    if Response == 0:
        DGWConnection = True
    else:
        DGWConnection = False
    if DGWConnection == True:
        print("\n***********************************************\n*** Default Gateway Connection Successful ***\n***********************************************\n")
    else:
        print("\n***********************************************\n*** Default Gateway Connection Failed ***\n***********************************************\n")
    #Sleeping for 2 Seconds
    time.sleep(2)

def DGWGetter(): #Default GateWay Getter Function (Only Prints the Default Gateway Address)
    """
    This function will grab the default gateway of the device when called.
    it will return the default gateway IP address.
    """
    #Cleaning the Terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    #   Grabbing the IP Default Gateway
    #get the default gateway using the route command
    route = subprocess.Popen(["route"], stdout=subprocess.PIPE)
    #use grep to filter the output to only show the default gateway
    grep = subprocess.Popen(["grep", "default"], stdin=route.stdout, stdout=subprocess.PIPE)
    #print the output of the default gateway
    output = grep.communicate()[0]
    #Getting the IP Address of the Default Gateway
    DGWAddr= socket.gethostbyname(output.decode('utf-8').split()[1]) #DGWAddr = Default GateWay Address
    #Testing the Default Gateway address Connection.
    print("\n***\n*** The Default Gateway Address is:- {}\n***".format(DGWAddr))
    #Sleeping for 2 Seconds
    time.sleep(2)

def RemoteIPTest(): #Remote IP Address Connectivity Testing Function
    """
    This function will test the connectivity to a remote IP address when called.
    it will return True if the connection is successful and False if it is not successful.
    """
    #Clean the Terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    #Testing an Remote IP address connectivity entered by the user.
    RemoteAddress = "129.21.3.17"
    print("\n")
    #Collecting the Response from the Server
    Response = os.system("ping -c 4 " + RemoteAddress)
    #Evaluating the Response from the Server
    if Response == 0:
        RAConnection = True
    else:
        RAConnection = False
    if RAConnection == True:
        print("\n***********************************************\n*** Remote IP Address Connection Successful ***\n***********************************************\n")
    else:
        print("\n********************************************\n*** Remote IP Address Connection Failed ***\n********************************************\n")
    #Sleeping for 2 Seconds
    time.sleep(2)

def DNSResolutionTest():#DNS (Domain Name Server) Connectivity Test.
    """
    This function will test the connectivity to a DNS server when called.
    it will take the DNS IP address test the connectivity to it and return True if the connection is successful and False if it is not successful.
    """
    #Clean the Terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    #Testing the DNS Resolution.
    DNSResoultion = "rit.edu"
    print("Trying to Resolve the DNS:- {}".format(DNSResoultion))
    time.sleep(2)
    try:
        DNSiP = socket.gethostbyname(DNSResoultion) #here we get the IP address of the DNS
        #If the provided URL Doesnt return any IP Address, then the DNS will be considered as down or invalid.
        if DNSiP == None:
            print("The IP Address of the DNS is:- 'NULL'")
            DNSConnectivity = False
        else:
            DNSConnectivity = True
    except:
        DNSConnectivity = False
    if DNSConnectivity == True:
        print("\nThe IP Address of the DNS is:- {}".format(DNSiP))
        time.sleep(1.5)
        print("\n*** DNS Connection Resolved Successfully ***\n")
    else:
        print("\nThe IP Address of the DNS is:- 'NULL'")
        time.sleep(1.5)
        print("\n*** DNS Connection Failed to Resolve ***\n")
    #Sleeping for 2 Seconds
    time.sleep(2)

def main(): #Main Function
    """
    This function will call all the other functions and will run the script.
    """
    WhileTerminator = -1
    while(WhileTerminator != 0): #Technichally a Do-While loop
        while True:
            #Menu for the user to select the test they want to perform.
            try:
                print("\n*************************************\n***** Welcome To Network Tester *****\n*************************************\n")
                print("[1] For Default Gateway Test")
                print("[2] Remote IP Address Test")
                print("[3] DNS Resolution Test")
                print("[4] To Print the Default Gateway Address")
                print("[Q] To Exit the Program ")
                #Strip white spaces
                TestChoice = str(input("\nPlease Enter Your Choice:- ").strip())
                break
            except:
                print("\n\n\n********************************************\n***** Invalid Input! Please Try Again! *****\n********************************************\n")
                time.sleep(1)
        #Evaluate the user input
        if(TestChoice == "1"):
            DGWGetterAndTest()
        if(TestChoice == "2"):
            RemoteIPTest()
        if(TestChoice == "3"):
            DNSResolutionTest()
        if(TestChoice == "4"):
            DGWGetter()
        if(TestChoice == "q" or TestChoice == "Q"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n**********************************************\n***** Thank You For Using Network Tester *****\n**********************************************\n")
            print("Quitting the Program in 3 Seconds...")
            time.sleep(3)
            #Terminates the While Loop and the Program
            WhileTerminator = 0
main()