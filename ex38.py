# Title: Exercise 38 - Doing Things to Lists
# from Learn Python the hard way
# Date: 3rd March 2017
# by Rimesh Jotaniya
# Description: Operations on List

ten_things = "Apples Orages Crows Telephone Light Sugar"

print "There's not ten things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There is %d items now" % len(stuff)

print "There we go: ", stuff

print "Let's do somethings with stuff."

print stuff[1]
print stuff[-1] # Whoa! fancy
print stuff.pop()
print ' '.join(stuff) # What? Cool!
print '#'.join(stuff[3:5]) # Super stellar!
