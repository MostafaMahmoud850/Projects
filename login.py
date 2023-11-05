# login by users
# pip install pystyle
from pystyle import * 
print(Box.Lines("[+] Learn python with Mostafa [+]"))
Write.Print("[+] this program for login page \n", Colors.purple_to_red, interval= 0.1)
Write.Print("[+] write user name and password \n\n", Colors.purple_to_red, interval= 0.1)
print(Box.DoubleCube("Example [1]"))

while True:
    username = Write.Input("write username :", Colors.blue_to_green, interval=0.1)
    password = Write.Input("write password :", Colors.blue_to_green, interval=0.1)
    if username == "Mostafa" and password == "90977":
        Write.Print("[+] welcome admin \n", Colors.green, interval= 0.1)
        input("press any key to exit ...")
    else:
        Write.Print("[-] Error Try again \n \n", Colors.red, interval= 0.1)