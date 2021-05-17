#!/usr/bin/env python3

#Imports
import subprocess
import os
import sys
import randmac
from randmac import RandMac
from getmac import get_mac_address

#ASCII Art
print("Made By Raghuram Subramani")
print("https://github.com/Stagefright071")
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

#pick a network card
cards = os.listdir('/sys/class/net/')
print(str(cards) + "\n")
network_card = input("What is the name of your network card?: ")

#main
current_mac = get_mac_address(interface=network_card)

print("\nYour Current Mac is: " + str(current_mac) + "\n")
option = input(
    '''
    Pick one:
    
    1. Random Mac

    2. Specific Mac (You will be asked to specify a Mac address)

    >'''
)

if option == "1":
    subprocess.call("ifconfig " + network_card + " down", shell=True)
    subprocess.call("ifconfig " + network_card+ " hw ether " + str(random_mac), shell=True)
    subprocess.call("ifconfig " + network_card + " up", shell=True)
elif option == "2":
    mac_address_chosen = input("\nWhat Mac do you want me to change your network card to? \n\n>")
    subprocess.call("ifconfig " + network_card + " down", shell=True)
    subprocess.call("ifconfig " + network_card+ " hw ether " + mac_address_chosen, shell=True)
    subprocess.call("ifconfig " + network_card +  " up", shell=True)
else:
    print("That's not a valid input.")

#exit
input("\nPress enter to exit ")
