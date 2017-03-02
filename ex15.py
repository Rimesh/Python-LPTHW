# Title: Exercise 15 - Reading Files
# from Learn Python the hard way
# Date: 2nd March 2017
# by Rimesh Jotaniya
# Description: reading a file and printing it.
# open(filename) returns object of filename
# read() returns contents of a fileObject

from sys import argv

script, filename = argv # reads filename from command line

text = open(filename) # open() returns a file object
#print type(text)

print "Here is your file %r:" % filename
print text.read()   # read() returns contents of a file object

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
