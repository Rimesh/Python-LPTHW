# Title: Exercise 7 - More Printing
# from Learn Python the hard way
# Date: 1st March 2017
# by Rimesh Jotaniya
# Description: in print statement, plus(+) concatenates and comma(,) concatenates with one space

print "Mary had a little lamb."
print "Its fleece was white as %s." % "snow"
print "And everywhere that Mary went."
print "." * 10 # what'd that do?        It prints 10 times continuously

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# after removing comma from the end
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12