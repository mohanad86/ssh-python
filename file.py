from sys import argv
import atexit
import os

script, filename = argv

def exit_handler():
    print ('Information Saved')


print ("Creating The File")
print ("\n")

config = open(filename, 'a')
scan = input("Scan Your network: ")
os.system("nmap -v " + scan + "/24" + "| grep " + " open ")
try:
    while True:
            first = input("Please Enter Machine Name: ")
            second = input("Please Enter The Hostname Of the Machine Or IP Address: ")
            third = input("Please Enter The Port Number. Skip with Enter: ")
            fourth = input("Please Enter The User: " )
            fifth = input("Copy the ssh id to the machine. Do you want to continue (y) ")
            sixth = input("Copy the ssh id to root. Do you want to continue (y):")
            if first:
                config.write("Host " + first)
                config.write("\n")
            if second:
                config.write("Hostname " + second)
                config.write("\n")
            if third: 
                config.write("Port " + third)
                config.write("\n")
            if fourth:
                config.write("User " + fourth)
                config.write("\n")
            if fifth:
                    os.system("ssh-copy-id " + fourth + "@" + second)
            if sixth:
                    os.system("ssh -t " + fourth + "@" + second  + " " + " " " 'sudo cp --parents .ssh/authorized_keys /root/' ")    
            print ("Finished and starting with the new machine")
            print ("\n")
            if first != fourth:
                config.write("\n")
                config.write("\n")
except KeyboardInterrupt:    
            config.close()
atexit.register(exit_handler)

