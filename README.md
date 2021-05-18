# Macchanger_py
A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. This use is common in most IEEE 802 networking technologies, including Ethernet, Wi-Fi, and Bluetooth.
Since Mac addresses are unique, changing them has many uses, example anonymity.

![image](https://user-images.githubusercontent.com/71056504/118467009-0c1d9080-b721-11eb-941a-7a5eb560d6f3.png)
![image](https://user-images.githubusercontent.com/71056504/118477925-e5fded80-b72c-11eb-84c9-296153b30e1b.png)
![image](https://user-images.githubusercontent.com/71056504/118478064-12b20500-b72d-11eb-94db-541b7a52e0bc.png)


To install, run install.sh according to your linux distro.

Windows and MacOS are NOT supported and will not work.

**_Install_**

> Run the respective install script as root.
```
git clone https://github.com/Stagefright071/Macchanger_py.git
sudo ./install-yourdistro
```

> Other distros or to install manually -

> Install git, python3, python3-pip, net-tools(ifconfig has to be present)
```
sudo python3 -m pip install -r requirements.txt
sudo cp bin/Macchanger.py /bin/macchangerpy
```
