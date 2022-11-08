#!/usr/bin/python

# Name: Muaz Osman
# STUDENT ID: mao3865
# DATE 02/10/2022
#Importing the modules
import csv , subprocess , os , re, time

#Declaring Lists to save the data
Groups = []
FirstName = []
LastName = []
UniqueUserName = []
EmployeeID = []
Office = []
Phone = []
EmployeeDepartment = []
Passwords = []
SystemUserNames = {}
Dupie = {}
BadUsers = []
IncorrectCollector= []
#Declaring the variables
numberofrow = 1 #Start from first row, increment by 1 so that the header is not read by the program
i = 0
PasswordChangeAttempt = 0
uniqueusername = ""
firstname = ""
lastname = ""
department = ""
group = ""
shelltype = ""
office = ""
phone = ""
password = ""
IncorrectInformationSkipper = False

#Take the users from the system and put them in a dictionary then use this dictionary to check if the username is already taken
#Open the /etc/passwd file and read it if the username is already taken then put it in the dictionary
for line in subprocess.check_output("sudo cat /etc/passwd", shell=True).decode("utf-8").splitlines():
    SystemUserNames[line.split(":")[0]] = line.split(":")[2]
#Take the names of the system users and put them in a dictionary then use this dictionary to check if the username is already taken
for key in SystemUserNames:
    #if the name already exists increment the value by 1
    if re.sub(r'\d+', '', key) in Dupie:
        Dupie[re.sub(r'\d+', '', key)] += 1 
    else:
        Dupie[re.sub(r'\d+', '', key)] = 0

#Clearing the Terminal before running the script.
os.system("clear")
print("Adding new users to the System...")
print("Please note that the default user Password is 'password' ")

NumberOfLines = sum(1 for line in open('linux_users.csv')) #Counting the number of lines in the CSV file
#Reading the CSV file
with open('linux_users.csv', 'r') as csv_file:
    csv_Reader = csv.DictReader(csv_file) #Setting the CSV file as a dictionary so that we can access the data using the column names
    for row in csv_Reader:
        IncorrectInformationSkipper = False
        numberofrow = numberofrow + 1 #Incrementing the number of row by 1 so that we can skip the header as required
        #Append the EmployeeID to its list
        EmployeeID.append(row['EmployeeID'])
        #if the Last Name is empty print that the information is incorrect and skip the cell and continue
        if row['LastName'] == '':
            IncorrectCollector.append("The information for the last name is Missing/Incorrect, " + str(numberofrow) + " EmployeeID: " + row['EmployeeID'])
            time.sleep(1)
            IncorrectInformationSkipper = True
            BadUsers.append("EmployeeID: " + row['EmployeeID'] + " Username: " + uniqueusername)
        else:
            LastName.append(row['LastName'])
        lastname = row['LastName']
        #if the First Name is empty print that the information is incorrect and skip the cell
        if row['FirstName'] == '':
            IncorrectCollector.append("The information for the First Name is Missing/incorrect, " + " EmployeeID: " + row['EmployeeID'])
            time.sleep(1)
            IncorrectInformationSkipper = True
            BadUsers.append(row['EmployeeID'])
        else:
            FirstName.append(row['FirstName'])
            firstname = row['FirstName']
        """"
        TODO:
        { 10/1/2022 }
        Check if the username is already taken and if it is then add a number to the end of the username : { DONE }
        Replace the special charachters : { DONE }
        Manage Duplicate Names : { DONE }
        """
        #Create the Unique User Name by combining the first letter of the first name and the last name
        username = firstname[0].lower() + lastname.lower()
        #Replace the special characters in the username using REGEX
        username = re.sub('[^A-Za-z0-9]+', '', username)
        i += 1
        #Check if the name is duplicate and if it is a duplicate add a number to the end of the username
            #if the user name is already in the list then add a number to the end of the username
        if username in Dupie:
                #Strip all the numbers from the username
            username = re.sub(r'\d+', '', username)
                #Append it to Dupie dictionary
            Dupie[username] += 1
            print("\nDuplicate username Found for: " + username + " Adding a number to the end of the username")
            username = username + str(Dupie[username])
        else:
            Dupie[username] = 0
        #Append the username to the list
        UniqueUserName.append(username)
        uniqueusername = username

        """
        TODO:
        { 10/2/2022 }
        Any member assigned to the “office” group must use “csh” (C shell) as their default shell, everyone else is assigned the Borne Again  Shell, or Bash as the default. { DONE }
        The script must detect incorrect data (e.g., what if the user's full name in the CSV file is '555-1212'? i.e., what if the person doing data entry made mistakes?).  You do not need to correct it, but the script should indicate that the record is invalid { DONE }
        Handle the Phone numbers, with the incorrect data, wrong format, etc. { DONE }
        Handle Departments { DONE }
        Groups and creating the groups { DONE }
        """
        #Office Handling, if the office has "-" in it then the information is correct, otherwise it is incorrect
        if (row['Office'].find('-') != -1):
            office = row['Office']
            Office.append(office)
        else:
            IncorrectCollector.append("The information for the Office is Missing/Incorrect, " + "EmployeeID:{}".format(row['EmployeeID']))
            time.sleep(1)
            IncorrectInformationSkipper = True
            BadUsers.append(row['EmployeeID'])
        #Phone Handling, if the cell is empty state that the information is incorrect and skip the row
        if row['Phone'] == '':
            IncorrectCollector.append("The information for the Phone is Missing/Incorrect, " + "EmployeeID:{}".format(row['EmployeeID']))
            time.sleep(1)
            IncorrectInformationSkipper = True
            BadUsers.append(row['EmployeeID'])
        #if the cell contains a "-" then the information is correct
        elif (row['Phone'].find('-') != -1) or (row['Phone'].find('unlisted') != -1):
            Phone.append(row['Phone'])
            phone = row['Phone']
        #else the information is incorrect
        else:
            IncorrectCollector.append("The information for the Phone is Missing/Incorrect, " + "EmployeeID:{}".format(row['EmployeeID']))
            time.sleep(1)
            IncorrectInformationSkipper = True
            BadUsers.append(row['EmployeeID'])
        #Department Handling.
        #if the cell is empty or contains "-" then the information is incorrect
        if row['Department'] == '' or (row['Department'].find('-') != -1):
            IncorrectCollector.append("The information for the Department is Missing/Incorrect, " + "EmployeeID:{}".format(row['EmployeeID']))
            time.sleep(1)
            IncorrectInformationSkipper = True
            BadUsers.append(row['EmployeeID'])
        else:
            EmployeeDepartment.append(row['Department'])
            department = row['Department']
        #Group Handling
        #if the value is pubsaftey or office or area51 then its correct information
        if row['Group'] == 'pubsafety' or row['Group'] == 'office' or row['Group'] == 'area51':
            Groups.append(row['Group'])
            group = row['Group']
        else:
            IncorrectCollector.append("The information for the Group is Missing/Incorrect, " + "EmployeeID:{}".format(row['EmployeeID']) +  " User:" + uniqueusername)
            time.sleep(1)
            group = "null"
            IncorrectInformationSkipper = True
            BadUsers.append(row['EmployeeID'])
        if group == 'office':
            shelltype = 'csh'
        else:
            shelltype = 'bash'
        #Set the default password to “password” for each new user, Expire the password so the first time the user logs in they must change it, For testing purposes use “1$4pizz@” as the password to change to.        
        password = "password"
        if IncorrectInformationSkipper == False:
            #Create the user, The user's home directory should be located in /home/department, where department is the user's department, e.g., for Natasha Richardson in the CEO department, the correct home directory would be /home/ceo/nrichardson in lowercase.
            try:
                os.system("sudo useradd -d /home/" + department.lower() + "/" + uniqueusername + " -m -s /bin/" + shelltype + " -p " + password + " " + uniqueusername)
                #Use os.system to change password to password with the command passwd
                os.system("echo " + uniqueusername + ":" + password + " | chpasswd")
            
            except:
                print("\nProcessing Employee ID " + row['EmployeeID'] + ".          " + uniqueusername + " was not created!")
                time.sleep(1)
            #Create the group if it does not exist
            try:
                #Check if the group exists using subprocess
                GroupEvlauation = os.system("sudo grep -q " + group + " /etc/group")
                if GroupEvlauation == 0:
                    print("\nGroup: " + group + " already exists!")
                    time.sleep(1)
                else:
                    print("\nGroup: " + group + " does not exist, creating group!")
                    time.sleep(1)
                    os.system("groupadd " + group)
            except:
                print("\nGroup: " + group + " does not exist, Creating the Group...")
                time.sleep(1)
                os.system("groupadd " + group)
            #Add the user to the group
            try:
                print("\nAdding the user: " + uniqueusername + " to the group: " + group + "...")
                time.sleep(1)
                os.system("sudo usermod -a -G " + group + " " + uniqueusername)
                print("\nUser: " + uniqueusername + " has been added to the group: " + group + "!")
            except:
                print("\nError Adding the user: " + uniqueusername + " to the group: " + group + "...")
                time.sleep(1)
            #Make the password expire so the user must change it on the first login
            try:
                time.sleep(1)
                PasswordEvaluation = os.system("sudo chage -d 0 " + uniqueusername)
                if PasswordEvaluation == 0:
                    print("\nPassword for user: " + uniqueusername + " has been set to expire!")
                    time.sleep(1)
                else:
                    print("\nPassword for user: " + uniqueusername + " has not been set to expire!")
                    time.sleep(1)
            except:
                print("\nError Making the password expire on next login for the user: " + uniqueusername + "...")
                time.sleep(1)
            #Changing the password to “1$4pizz@” for testing purposes only for one user.
            if PasswordChangeAttempt == 0:
                try:
                    print("\nTrying to Change the password for the user: " + uniqueusername + "...")
                    time.sleep(1)
                    newpassword = "1$4pizz@"
                    #change the password to 1$4pizz@ after the first login
                    PasswordEvaluation = subprocess.run(['su', uniqueusername], input='password\n1$4pizz@\n1$4pizz@', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    print("The new password for the user: " + uniqueusername + " is: 1$4pizz@")
                except:
                    print("\nError Changing the password for the user: " + uniqueusername + "...")
                    time.sleep(1)
                PasswordChangeAttempt += 1
BadUsers = set(BadUsers) #Removing the DUplciates
for BadUser in BadUsers:
    print("\nProcessing Employee ID " + BadUser + ".          " + "Employee ID :" + BadUser + " was not created!")
    time.sleep(0.5)
for IncorrectStatement in IncorrectCollector:
    print("\n" + IncorrectStatement)
    time.sleep(0.5)
#Close the file to prevent memory leaks
csv_file.close()