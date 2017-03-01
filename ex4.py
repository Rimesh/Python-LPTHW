# Title: Exercise 4 - Variables and Names
# from Learn Python the hard way
# Date: 1st March 2017
# by Rimesh Jotaniya
# Description: Learn to use variables 

cars = 100              # Number of cars available
space_in_a_car = 4      # Capacity of a car is 4 passengers
drivers = 30            # We have total 30 drivers available
passengers = 90         # There are total 90 passengers
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "we can transport", carpool_capacity, "people today"
print "we have", passengers, " passengers to carpool today"
print "we need to put about", average_passengers_per_car, "in each car"
