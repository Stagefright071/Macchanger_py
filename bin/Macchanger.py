#!/usr/bin/env python3

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

#Imports
import subprocess

#Main
wireless_card = input("What is the name of your network card?: ")
mac_address = input("What do you want the mac address to be?: ")

subprocess.call("ifconfig " + wireless_card + " down", shell=True)
subprocess.call("ifconfig " + wireless_card+ " hw ether " + mac_address, shell=True)
subprocess.call("ifconfig " + wireless_card +  " up", shell=True)

input("Press enter to exit ")