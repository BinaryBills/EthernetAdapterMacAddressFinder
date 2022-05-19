#Author: Binary Bills
#Creation Date: May 9, 2022
#Modification Date: May 14, 2022
#Purpose: This program runs the command "ipconfig /all" from the user's terminal and searches for the mac address associated with the ethernet adapter currently plugged into their system.
import subprocess
import os
import time
import threading
import winsound
import platform
from time import sleep

#Runs the file "m.wav" from its directionary
def playMusic():
    winsound.PlaySound("m.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )

#Saves the result from "ipconfig.all" into a txt file
def saveIPConfig():
    ipConfigAllData = subprocess.getoutput("ipconfig /all")
    textfile = open("ipConfig.txt", "w")
    a = textfile.write(ipConfigAllData)
    textfile.close()

#Searches for the mac address of the ethernet adapter
def findMacAddress():
 saveIPConfig()
 loop = False
 found = False
 print("RESULT: ")
 print("")
 with open("ipConfig.txt", "r") as test_file:
    for line in test_file:
        if "Ethernet adapter Ethernet" in line:
            print(line)
            loop = True
            found = True
        if loop == True:
            if "Physical" in line:
             print(line)
             print("")
             loop = False
 return found
        
#Clears the window by printing multiple lines
def clearWindow():
    print('\n' * 50)

def mainMenu():
 
    menu = """
8===================================================================================================================8
 ____  _                          ____  _ _ _ _       ______ _   _                          _   
 |  _ \(_)                        |  _ \(_) | ( )     |  ____| | | |                        | |  
 | |_) |_ _ __   __ _ _ __ _   _  | |_) |_| | |/ ___  | |__  | |_| |__   ___ _ __ _ __   ___| |_ 
 |  _ <| | '_ \ / _` | '__| | | | |  _ <| | | | / __| |  __| | __| '_ \ / _ \ '__| '_ \ / _ \ __|
 | |_) | | | | | (_| | |  | |_| | | |_) | | | | \__ \ | |____| |_| | | |  __/ |  | | | |  __/ |_ 
 |____/|_|_| |_|\__,_|_|   \__, | |____/|_|_|_| |___/ |______|\__|_| |_|\___|_|  |_| |_|\___|\__|
  __  __          _____     __/ |  _____  _____  _____  ______  _____ _____                      
 |  \/  |   /\   / ____|   |_/\/  |  __ \|  __ \|  __ \|  ____|/ ____/ ____|                     
 | \  / |  /  \ | |         /  \  | |  | | |  | | |__) | |__  | (___| (___                       
 | |\/| | / /\ \| |        / /\ \ | |  | | |  | |  _  /|  __|  \___ \\___ \                      
 | |  | |/ ____ \ |____   / ____ \| |__| | |__| | | \ \| |____ ____) |___) |                     
 |_|__|_/_/___ \_\_____|_/_/_ __\_\_____/|_____/|_|__\_\______|_____/_____/                      
 |  __ \|  __ \ / __ \ / ____|  __ \     /\   |  \/  |                                           
 | |__) | |__) | |  | | |  __| |__) |   /  \  | \  / |                                           
 |  ___/|  _  /| |  | | | |_ |  _  /   / /\ \ | |\/| |                                           
 | |    | | \ \| |__| | |__| | | \ \  / ____ \| |  | |                                           
 |_|    |_|  \_\\____/ \_____|_|  \_\/_/    \_\_|  |_| 
 By: https://github.com/BinaryBills
8===================================================================================================================8

o8==========8o                                                   o8==========8o                                                                
 |    (1)   |                                                     |   (2)    |
 |   BEGIN  |                                                     |   EXIT   |
o8==========8o                                                   O8==========8O 
    """
    print(menu)
   

playMusic()

while (True):
    mainMenu()
    userChoice = input("Please enter one of the following options: ")

    if userChoice == "1":
        if findMacAddress() == False:
            print("Your ethernet adapter is either not plugged in or detected.")
            os.system("pause")
            clearWindow()
        else:
            print("SUCCESS")
            os.system("pause")
            clearWindow()
    elif userChoice == "2":
        print("Thank you for using my program!")
        break
    else:
        print("Enter a valid input")

 
