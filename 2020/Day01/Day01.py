#!/usr/bin/env python3

#open file
print("Opening File...")
inputfile = open('input', 'r')

#count lines
numlines = inputfile.readline()
count = 0
filecontent = [0]
while numlines:
    filecontent.append(int(float(numlines)))
    numlines = inputfile.readline()
    count += 1
print ("File has ", count, " lines")

#Start Outer Loop
sumfound = False
x = 0
while x < count:
    entry_x = filecontent[x]
    y = count
    #start Inner Loop
    while y > x:
        entry_y = filecontent[y]
        sum_xy = entry_x + entry_y
        print("Sum of Line ",x," and ",y," :  ",entry_x," + ",entry_y," = ",sum_xy)
        y -= 1
        if sum_xy == 2020:
            y = count
            x = count
            sumfound = True
    x += 1
if sumfound: print("Product = ",entry_x * entry_y)
else: print("No lines summed to 2020")

#close file, we're done with it
print("...Closinging File")
inputfile.close() 
