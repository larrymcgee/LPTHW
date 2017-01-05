# imports madule argv
from sys import argv

# assigns command line arguments to script and filename
script, filename = argv

# opens file and assigns to txt
txt = open(filename)

#prints the name of the file and the file contents
print "Here's your file %r:" % filename
print txt.read()

txt.close()
# prompts user to enter filename
print "Type the filename again:"
file_again = raw_input("> ")

# opens the file_again
txt_again = open(file_again)

# prints contents of txt_again
print txt_again.read()
txt_again.close()
