from geoip import geolite2
import re
from datetime import date

#Clear Terminal Linux
print(chr(27) + "[2J")

# Define the Variables
IP_Address = {}
IP_Address_Country = []

# Print the Header and todays date
print("\n"+"Attacker Report - {}".format(date.today().strftime("%B %d, %Y")))

# Printing the Header
print("\nCOUNT        IP ADDRESS     COUNTRY")

# Opening the file
with open('syslog.log') as Log:
    # Loop through the file
    for line in Log:
        # Find the FAILED LOGIN IP Addresses using Regex Editor
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
            # Get The Current Index of the IP Address
            Index = list(IP_Address.keys()).index(i)
            # Get the Country of the IP Address
            Country = IP_Address_Country[Index]
            print("{0:10}  {1:15}   {2:15}".format(str(IP_Address[i]), i, Country))
        else:
            pass

# Close the file to prevent memory leaks
Log.close()
