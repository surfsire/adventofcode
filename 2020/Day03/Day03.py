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


path_product = 1
i = 5
while (i > 0):
    x_coord = 1 #x starting point
    y_coord = 1 #y starting point
    if (i == 5):
        x_incr = 1  #x increment
        y_incr = 1  #y increment
    if (i == 4):
        x_incr = 3  #x increment
        y_incr = 1  #y increment
    if (i == 3):
        x_incr = 5  #x increment
        y_incr = 1  #y increment
    if (i == 2):
        x_incr = 7  #x increment
        y_incr = 1  #y increment
    if (i == 1):
        x_incr = 1  #x increment
        y_incr = 2  #y increment
        
    tree_cnt = 0
    while (y_coord <= count):
        entry_x = filecontent[y_coord]
        if (x_coord > 31): x_coord -= 31                #Map/Pattern is 32 columns; 0-31
        if (entry_x[x_coord-1] == "#"): tree_cnt += 1   #increment tree count if # is found 
        x_coord += x_incr
        y_coord += y_incr

    path_product *= tree_cnt
    print("Path ",i," there were", tree_cnt, " trees\t Product=", path_product)
    i -= 1

#close file, we're done with it
print("...Closinging File")
inputfile.close() 