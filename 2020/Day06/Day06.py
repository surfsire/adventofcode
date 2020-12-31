#!/usr/bin/env python3

#open file
print("Opening File...")
inputfile = open('input', 'r')

#count lines
numlines = inputfile.readline()
count = 0
filecontent = [0]
while numlines:
    filecontent.append(numlines)
    numlines = inputfile.readline()
    count += 1
print ("File has ", count, " lines")

max_val = 0
i = 1
while (i <= count):
    entry_x = filecontent[i]

    i += 1

#print("Largest Value was:",max_val)
print("Answer.")


#close file, we're done with it
print("...Closing File")
inputfile.close() 