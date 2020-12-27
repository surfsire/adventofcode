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

x_coord = 1 #x starting point
x_incr = 3  #x increment
y_coord = 1 #y starting point
y_incr = 1  #y increment

tree_cnt = 0
while (y_coord <= count):
    entry_x = filecontent[y_coord]
    if (x_coord > 31): x_coord -= 31                #Map/Pattern is 32 columns
    if (entry_x[x_coord-1] == "#"): tree_cnt += 1   #increment tree count if # is found 
    x_coord += x_incr
    y_coord += y_incr

print("There were", tree_cnt, "trees down the path")

#close file, we're done with it
print("...Closinging File")
inputfile.close() 