#!/usr/bin/env python3

#Imports
import subprocess
import os
import sys
import randmac
from randmac import RandMac
from getmac import get_mac_address
import re

#ASCII Art
print("Made By Raghuram Subramani")
print("https://github.com/compromyse")
print('''
███╗░░░███╗░█████╗░░█████╗░░█████╗░██╗░░██╗░█████╗░███╗░░██╗░██████╗░███████╗██████╗░░░░██████╗░██╗░░░██╗
████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗░░░██╔══██╗╚██╗░██╔╝
██╔████╔██║███████║██║░░╚═╝██║░░╚═╝███████║███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝░░░██████╔╝░╚████╔╝░
██║╚██╔╝██║██╔══██║██║░░██╗██║░░██╗██╔══██║██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗░░░██╔═══╝░░░╚██╔╝░░
██║░╚═╝░██║██║░░██║╚█████╔╝╚█████╔╝██║░░██║██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║██╗██║░░░░░░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░
''')

#Check if user is root
if not os.geteuid()==0:
    sys.exit('This script must be run as root!')
else:
    print("User is root, the script can continue...\n")

#Generate random mac
random_mac = RandMac()


#function
def mac_change_random(network_card, random_mac):
    subprocess.call(["ifconfig", network_card, "down"])
    subprocess.call(["ifconfig", network_card, "hw", "ether", str(random_mac)])
    subprocess.call(["ifconfig", network_card, "up"])
    final_mac = random_mac

def mac_change_specific(network_card, specified_mac):
    subprocess.call(["ifconfig", network_card, "down"])
    subprocess.call(["ifconfig", network_card, "hw", "ether", specified_mac])
    subprocess.call(["ifconfig", network_card, "up"])
    final_mac = specified_mac

#pick a network card
cards = os.listdir('/sys/class/net/')
for i in cards:
    print(f'{i}\n')
network_card = input("What is the name of your network card?: ")

#fiter out lo
if network_card == "lo":
    print("\nThat interface is not allowed")
    exit(0)

#Get original mac
ifconfig_output = subprocess.check_output(["ifconfig", network_card])
original_mac_result = re.search( r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))
original_mac = original_mac_result.group(0)

#Check if original mac contains a value
if original_mac:
    pass
else:
    print("Could not read MAC address.")
    exit(0)

#main
current_mac = get_mac_address(interface=network_card)

print("\nYour Current Mac is: " + str(current_mac) + "\n")
#Options
option = input(
    '''
    Pick one:
    
    1. Random Mac

    2. Specific Mac (You will be asked to specify a Mac address)

    >''' 
)

#Option results
if option == "1":
    mac_change_random(network_card, random_mac)
    if original_mac == random_mac:
        print("MAC address could not be changed...\n\nexiting now..")
        exit(0)
    elif original_mac != random_mac:
        print("\nMAC address has been changed to " + str(random_mac))
    else:
        print("Unidentified error")
elif option == "2":
    specified_mac = input("What do you want to change the MAC address to?\n\n >")
    mac_change_specific(network_card, specified_mac)
    if original_mac == specified_mac:
        print("MAC address could not be changed...\n\nexiting now..")
        exit(0)
    elif original_mac != specified_mac:
        print("\nMAC address has been changed to " + str(specified_mac))
    else:
        print("Unidentified error")
#Input validation
else:
    print("That's not a valid input.")

#exit
input("\nPress enter to exit ")
