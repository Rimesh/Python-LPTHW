# Title: Exercise 32 - Loops and Lists
# from Learn Python the hard way
# Date: 3rd March 2017
# by Rimesh Jotaniya
# Description: For loop and list

the_count = [ 1, 2, 3, 4, 5]
fruits = ["apple", "orange", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count: %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Also, we can go through a mixed list too
# notice, we have to use %r since we don't know what is in it.
for i in change:
    print "I got %r" % i

# We can also build list, first start with an empty one.
elements = []

#then use range function to do 0 to 5 coounts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understands
    elements.append(i)

# Now we can print them out too
for i in elements:
    print "element was: %d" % i
