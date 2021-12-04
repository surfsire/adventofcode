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

#Start Scan of Each Line - Part 1
total_inc = 0; #Total measurements larger than last [puzzle goal - part 1]
for x in range(count-1):
    entry_x = filecontent[x]
    entry_y = filecontent[x + 1]
    if (entry_y > entry_x):
        total_inc += 1
        #print(x+1," Increasing -- ",entry_y," > ",entry_x,"\t",total_inc," total found")

#Start Scan of Each Line - Part 2
total_slide = 0; #Total measurements larger than last [puzzle goal - part 2]
for x in range(count-3):
    slide_x = filecontent[x] + filecontent[x+1] + filecontent[x+2]
    slide_y = filecontent[x+1] + filecontent[x+2] + filecontent[x+3]
    if (slide_y > slide_x):
        total_slide += 1
        #print(x+1," to ",x+3," Increasing -- ",slide_y," > ",slide_x,"\t",total_slide," total found")

print("\n\033[0;34m !=== ANSWERS ===! \033[0m")
print("PART I  \tA TOTAL of \033[0;32m",total_inc,"\033[0m increasing measurements were found") #Puzzle Answer #1
print("PART II \tA TOTAL of \033[0;32m",total_slide,"\033[0m increasing slide measurements were found") #Puzzle Answer #2

#close file, we're done with it
print("\n...Closing File")
inputfile.close() 
