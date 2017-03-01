# Title: Exercise 11 - Asking questions
# from Learn Python the hard way
# Date: 1st March 2017
# by Rimesh Jotaniya
# Description: Take some kind of input from a person.

print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weight?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy." % (age, height, weight)
