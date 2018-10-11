from sys import argv

script, input_file = argv

def print_all(f):
    print ("This is line 1\nThis is line 2\nThis is line 3\n")

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
     print ("This is line 1\n\nThis is line 2\n\nThis is line 3\n\n")

current_file = open(input_file)

print ("First let's print the whole file:\n")

print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

rewind(current_file)

print ("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)