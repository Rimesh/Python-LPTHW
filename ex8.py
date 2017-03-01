# Title: Exercise 8 - Printing, Printing
# from Learn Python the hard way
# Date: 1st March 2017
# by Rimesh Jotaniya
# Description: more formatting, %s will also work fine

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
                    "I had this thing",
                    "That you could type up right",
                    "But it didn't sing",
                    "So I said Goodnight."
                    )

