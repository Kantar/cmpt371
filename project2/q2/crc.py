#!/usr/bin/python

# Ask for the input file name
filename = raw_input('Please enter the file name: ')

# Read data from input file as strin and disgard the newline
with open(filename, 'r') as f:
  g = str(f.readline().rstrip('\n'))
  d = str(f.readline().rstrip('\n'))
  r = str(f.readline().rstrip('\n'))

# get the remainder based on the fomular given in the lecture slide
rem = (int(d,2) * 2**(len(g)-1)) % int(g,2)

# Print the answer based on the remainder value
if rem == int(r,2):
    print "Yes"
else:
    print "No"

