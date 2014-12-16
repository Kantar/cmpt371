#!/usr/bin/python

from decimal import *

# Ask for the input file name
filename = raw_input('Please enter the file name: ')

# Read data from input file 
with open(filename, 'r') as f:
    line = f.readline()

# Get the input and store them to a list
list = map(int, line.split(','))
print "Here is your input:", list


# Ensure we are given at least minimum element in the input
if len(list) < 2:
    print ("Not enough arguements are give. Bye!")
else: 
    # Create a constant object to print output with 2 decimal
    TWOPLACES = Decimal(10) ** -2

    # Replacing the first input with the given est_rtt0 as 100
    list[0] = 100

    # Perform calculation       
    for elem in range(0,(len(list)-1)):
      # Ensure elem+1 won't be out of index
      if len(list) >= (elem+1):
        est_rtt = (1-0.125)*list[elem]+0.125*list[elem+1]

        # Format each est_rtt to be 2 decimal 
        est_rtt = float("{0:.2f}".format(est_rtt,2))

        # Converting the type to be float so that calculation can be continued
        list[elem+1] = est_rtt

        # Ensure all estimated rtt is printed with 2 decimals
        estimated_rtt = Decimal(est_rtt).quantize(TWOPLACES)

        # Print each estimated rtt
        print "Estimated RTT" , elem+1, " is: ", estimated_rtt
