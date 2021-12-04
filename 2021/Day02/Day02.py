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

#Start Scan of Each Line - Part 1
position_x = 0; #Current Horizontal Position [part of puzzle goal - part 1]
position_z = 0; #Current Depth [part of puzzle goal - Part 1]
x = 1
while (x < count + 1):
    entry_x = filecontent[x].split()
    if   ( entry_x[0] == "forward"):
        position_x += int(float(entry_x[1]))
    elif ( entry_x[0] == "down"):
        position_z += int(float(entry_x[1]))
    elif ( entry_x[0] == "up"):
        position_z += 0-int(float(entry_x[1]))
        if (position_z < 0 ): position_z = 0
    else:
        print("\033[31m BAD INPUT @ Line", x,"\033[0m")
    #print(entry_x,"Moved to Position = ",position_x,position_z)
    x += 1

#Start Scan of Each Line - Part 2
position_x2 = 0; #Current Horizontal Position [part of puzzle goal - part 2]
position_z2 = 0; #Current Depth [part of puzzle goal - Part 2]
position_aim = 0; #Current Aim [part of puzzle goal - Part 2]
x = 1
while (x < count + 1):
    entry_x = filecontent[x].split()
    if   ( entry_x[0] == "forward"):
        position_x2 += int(float(entry_x[1]))
        position_z2 += int(float(entry_x[1])) * position_aim
    elif ( entry_x[0] == "down"):
        position_aim += int(float(entry_x[1]))
    elif ( entry_x[0] == "up"):
        position_aim += 0-int(float(entry_x[1]))
    else:
        print("\033[31m BAD INPUT @ Line", x,"\033[0m")
    print(entry_x,"Moved to Position",position_x2,position_z2," Move Aim to", position_aim)
    x += 1

print("\n\033[0;34m !=== ANSWERS ===! \033[0m")
print("PART I  \tFinal Horizontal: \033[0;33m",position_x,"\033[0m Final Depth: \033[0;33m",position_z,"\033[0m -- Product: \033[0;32m",position_x * position_z,"\033[0m") #Puzzle Answer #1
print("PART II \tFinal Horizontal: \033[0;33m",position_x2,"\033[0m Final Depth: \033[0;33m",position_z2,"\033[0m --Product: \033[0;32m",position_x2 * position_z2,"\033[0m") #Puzzle Answer #2

#close file, we're done with it
print("\n...Closing File")
inputfile.close() 
