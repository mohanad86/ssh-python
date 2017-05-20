from sys import argv

script, filename = argv


print "Creating The File"
config = open(filename, 'a')


try:
    while True:
            first = raw_input("Please Enter Machine name: ")
            second = raw_input("Please Enter The Hostname Of the Machine Or IP Address: ")
            third = raw_input("Please Enter The Port Number. Skip with Enter: ")
            fourth = raw_input("Please Enter The User : ")
            if first:
                config.write("Host " + first)
                config.write("\n")
            config.write("Hostname " + second)
            config.write("\n")
            if third: 
                config.write("Port " + third)
                config.write("\n")
            config.write("User " + fourth)
            config.write("\n")
            print "Finish"
            config.write("\n")
            config.write("\n")
except KeyboardInterrupt:    
            config.close()
