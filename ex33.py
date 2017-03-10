# Title: Exercise 33 - While-Loops
# from Learn Python the hard way
# Date: 3rd March 2017
# by Rimesh Jotaniya
# Description: Introduction to while loops

def loopme(count):
    i = 0
    numbers = []
    
    while i < count:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + 1
        print "Numbers now: ", numbers
        
        print "At the bottom i is %d" % i
    
loopme(5)

