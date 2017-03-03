# Title: Exercise 21 - Functions Can Return Something
# from Learn Python the hard way
# Date: 2nd March 2017
# by Rimesh Jotaniya
# Description: returning values from a function

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract (a, b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "let's do some math with just functions!"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(33, 2)
iq = divide(100, 2)

print "Age: %d, height: %d, weight: %d and IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it anyway.
print "Here is a puzzle"

what = add(age, subtract (height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
