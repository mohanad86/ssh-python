from sys import argv
import atexit

script, filename = argv

def exit_handler():
    print 'Information Saved'



print "Creating The File"
print "\n"

config = open(filename, 'a')


try:
    while True:
            first = raw_input("Please Enter Machine Name: ")
            second = raw_input("Please Enter The Hostname Of the Machine Or IP Address: ")
            third = raw_input("Please Enter The Port Number. Skip with Enter: ")
            fourth = raw_input("Please Enter The User : ")
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
            print "Finished and starting with the new machine"
            print "\n"
            if first != fourth:
                config.write("\n")
                config.write("\n")
except KeyboardInterrupt:    
            config.close()
atexit.register(exit_handler)

