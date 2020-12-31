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
    entry_x = entry_x[:entry_x.find("/n")]
    entry_x = entry_x.replace("B","1")
    entry_x = entry_x.replace("F","0")
    entry_x = entry_x.replace("R","1")
    entry_x = entry_x.replace("L","0")
    print("Line ",i,"\t",filecontent[i],entry_x,"=",int(entry_x,2))
    if (int(entry_x,2)) > (max_val): max_val = int(entry_x,2)
    i += 1

print("Largest Value was:",max_val)


#close file, we're done with it
print("...Closing File")
inputfile.close() 