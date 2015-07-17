while True: # infinit loop unless hit the break key word
    input = raw_input("Type something? ")
    if input.lower() == 'quit':
        break # break the CURRENT loop
    print "Are you saying: {}".format(input)
    
print "Goodbye"