outter_loop_index = 0;
for word in "Hello world!".split():
    inner_loop_index = 0
    for letter in word:
        print "<{},{}> {}".format(outter_loop_index, inner_loop_index, letter.upper())
        inner_loop_index += 1
    outter_loop_index += 1
