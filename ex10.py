# Title: Exercise 10 - What was that
# from Learn Python the hard way
# Date: 1st March 2017
# by Rimesh Jotaniya
# Description: learn about escape characters

tabby_cat = "\tI am tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """           
I'll do a list:
\t* cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""     # we can use '''(triple- single- quote) also

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# while True:
#    for i in ["/","- ","|","\\","|"]:
#        print "%s\r" % i,
