# Title: Exercise 18 - Names, Variables, Code, Functions
# from Learn Python the hard way
# Date: 2nd March 2017
# by Rimesh Jotaniya
# Description: Defining functions with and without arguments

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)
    
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
    print "I got nothing."
    
print_two("Rimesh","Jotaniya")
print_two_again("Rimesh","Jotaniya")
print_one("Rimesh!")
print_none()
