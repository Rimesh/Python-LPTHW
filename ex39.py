# Title: Exercise 39 - Dictionaries, Oh Lovely Dictionaries
# from Learn Python the hard way
# Date: 10th March 2017
# by Rimesh Jotaniya
# Description: Introduction to Dictionaries

# create a mapping of state to abbreviation
states = {
    'Gujarat': 'GJ',
    'Maharashtra': 'MH',
    'Rajasthan': 'RJ',
    'Karnataka': 'KA',
    'Punjab': 'PB'
    }

# create a basic set of states and some cities in them
cities = {
    'GJ': 'Surat',
    'MH': 'Mumbai',
    'RJ': 'Jaipur'
    }

# add some more cities
cities['KA'] = 'Bangluru'
cities['PB'] = 'Amritsar'

# print out some cities
print '-' * 10
print "MH state has: ", cities['MH']
print "GJ state has: ", cities['GJ']

# print some states
print '-' * 10
print "Karnataka's abbreviation is: ", states['Karnataka']
print "Punjab's abbreviation is: ", states['Punjab']

# do it by using states and then cities dict
print '-' * 10
print "Maharashtra has: ", cities[states['Maharashtra']]
print "Gujarat has: ", cities[states['Gujarat']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."
    
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
