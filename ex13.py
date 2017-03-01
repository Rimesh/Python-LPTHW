# Title: Exercise 13 - Parameters, Unpacking, Variables
# from Learn Python the hard way
# Date: 1st March 2017
# by Rimesh Jotaniya
# Description: taking command line arguments

from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
