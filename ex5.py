# Title: Exercise 5 - More Variables and Printing
# from Learn Python the hard way
# Date: 1st March 2017
# by Rimesh Jotaniya
# Description: using formatters (%s Strings) (%d Numeric) (%r raw data)

my_name = 'Rimesh Jotaniya'
my_age = 24 # Years
my_height = 74 # inches
my_weight = 66 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "he is %d inches tall" % my_height
print "He is %d kgs heavy" % my_weight
print "Actually that's not too heavy"
print "he has got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

#this line is tricky try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)
