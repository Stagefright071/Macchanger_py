# Macchanger_py
A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. This use is common in most IEEE 802 networking technologies, including Ethernet, Wi-Fi, and Bluetooth.
Since Mac addresses are unique, changing them has many uses, example anonymity.

![image](https://user-images.githubusercontent.com/71056504/118467009-0c1d9080-b721-11eb-941a-7a5eb560d6f3.png)

To install, run install.sh according to your linux distro.

Windows and MacOS are NOT supported. MacOS might work but is not tested

---INSTALL---

Run the respective install script as root.
```
git clone https://github.com/Stagefright071/Macchanger_py.git
sudo ./install-yourdistro
```

Other distros or to install manually -

install git, python3, python3-pip, net-tools(ifconfig has to be present)
```
sudo python3 -m pip install -r requirements.txt
sudo cp bin/Macchanger.py /bin/macchangerpy
```
