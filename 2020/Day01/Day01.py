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
x = 1
while (x < (count - 2)):
    entry_x = filecontent[x]
    y = x + 1
    #Start Mid Loop
    while (y < (count - 1)):
        entry_y = filecontent[y]
        z = count
        #start Inner Loop
        while z > y:
            entry_z = filecontent[z]
            sum_xyz = entry_x + entry_y + entry_z 
            if sum_xyz == 2020:
                print("Sum of Line ",x,", ",y,",and ",z,", :  ",entry_x," + ",entry_y,"+",entry_z," = ",sum_xyz)
                z = count
                y = count
                x = count
                sumfound = True
            z -= 1
        y += 1
    x += 1
if sumfound: print("Product = ",entry_x * entry_y * entry_z)
else: print("No lines summed to 2020")

#close file, we're done with it
print("...Closinging File")
inputfile.close() 
