from geoip import geolite2
import re
from datetime import date
"""
TODO:
    Variables i might need:
        1- A dictionary to store the IP Addresses at, and count them since we can use the Dictionary key to increment the count
        we can use the Dictionary to sort the IP Addresses by count, alredy a thing in Dictionaries

    What im thinking about is, Loop through the file, find the IP address using Regex Editor, Add the found IP addresses to the dictionary
    and if they are repeated increment the Key of the dictionary (Using a dictionary saves alot of time and its easier to implement),
    After that take every IP Address and check the IP Address origin and Save it in a List/Variable depending on how i will implement the script,
    After that i will sort the IP Addresses by count and print them out in a format.
"""
#Define the Variables
IP_Address = {}
IP_Address_Country = []

#Print the Header and todays date
print("\n"+"Attacker Report - {}".format(date.today().strftime("%B %d, %Y")))

#Printing the Header
print("\nCOUNT        IP ADDRESS     COUNTRY")

# Open the file
with open('syslog.log') as Log:
    # Loop through the file
    for line in Log:
        # Find the IP Address using Regex Editor and add it to the Dictionary
        IP = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line)
        for i in IP:
            if i in IP_Address:
                IP_Address[i] += 1
            else:
                IP_Address[i] = 1

    # Loop through the Dictionary and Check the IP Address Origin
    for i in IP_Address:
        match = geolite2.lookup(i)
        if match is not None:
            IP_Address_Country.append(match.country)
        else:
            IP_Address_Country.append("Unknown")

    # Print from smallest to largest order of count.
    for i in sorted(IP_Address, key=IP_Address.get):
        if IP_Address[i] > 10:
            #Get The Current Index of the IP Address
            Index = list(IP_Address.keys()).index(i)
            #Get the Country of the IP Address
            Country = IP_Address_Country[Index]
            print("{0:10}  {1:15}   {2:15}".format(str(IP_Address[i]), i, Country))
        else:
            pass

#Close the file to prevent memory leaks
Log.close()
