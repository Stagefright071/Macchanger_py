# Macchanger_py
A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. This use is common in most IEEE 802 networking technologies, including Ethernet, Wi-Fi, and Bluetooth.
Since Mac addresses are unique, changing them has many uses, example anonymity.

```
Made By Raghuram Subramani
https://github.com/Stagefright071

███╗░░░███╗░█████╗░░█████╗░░█████╗░██╗░░██╗░█████╗░███╗░░██╗░██████╗░███████╗██████╗░░░░██████╗░██╗░░░██╗
████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗░░░██╔══██╗╚██╗░██╔╝
██╔████╔██║███████║██║░░╚═╝██║░░╚═╝███████║███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝░░░██████╔╝░╚████╔╝░
██║╚██╔╝██║██╔══██║██║░░██╗██║░░██╗██╔══██║██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗░░░██╔═══╝░░░╚██╔╝░░
██║░╚═╝░██║██║░░██║╚█████╔╝╚█████╔╝██║░░██║██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║██╗██║░░░░░░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░

User is root, the script can continue...

virbr0

vmnet1

virbr0-nic

vmnet8

wlp0s20f3

docker0

enp2s0

lo

What is the name of your network card?: enp2s0

Your Current Mac is: 00:11:22:33:44:55


    Pick one:
    
    1. Random Mac

    2. Specific Mac (You will be asked to specify a Mac address)

    >1

MAC address has been changed to 62:06:a5:5d:50:bb

Press enter to exit 
```
# Running

> Install python and git
```
Debian / Ubuntu based: $ sudo apt install python3 python3-pip git

Arch based: $ sudo pacman -S python python-pip
```

> Clone git repository
```
git clone https://github.com/Stagefright071/Macchanger_py
```

> Install script requirements
```
python3 -m pip install -r requirements.txt
```

> Run the script as **root**
```
sudo python3 Macchanger.py
```

# Thanks!