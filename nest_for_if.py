my_string = raw_input("Type something: ")

num_of_letter_a = 0
num_of_letter_e = 0
for word in my_string.split():
    for letter in word:
        if letter.upper() == 'A':
            num_of_letter_a += 1
        elif letter.upper() == 'E':
            num_of_letter_e += 1
if num_of_letter_a > 0:
    print "Your input has contains Letter a {} times".format(num_of_letter_a)
else:
    print "Your input does not contains any Letter a"

if num_of_letter_e > 0:
    print "Your input has contains Letter e {} times".format(num_of_letter_e)
else:
    print "Your input does not contains any Letter e"

