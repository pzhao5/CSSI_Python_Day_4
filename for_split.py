my_string = raw_input("Type something: ")

# upper() method on string would capitalize the string.
# print "{} {}".format("", "") is the way to format a string.
# Unlike JS, Python does not support ++, thus you should use += 1 instead

print "Print words in upper case"
index = 0
for word in my_string.split(): # return individual words in a string. Split it by white space
    print "{} {}".format(index, word.upper())  # capitalize the words
    index += 1

print "Print each letter upper case"
index = 0
for letter in my_string:
    print "{} {}".format(index, letter.upper())
    index += 1
