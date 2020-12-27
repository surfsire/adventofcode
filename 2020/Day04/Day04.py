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

i=1
passport_all = ""
valid_fields = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
valid_count = 0
total_passports = 0
while (i <= count):
    entry_x = filecontent[i]
    if ((entry_x != "\n")):
        newline_index = entry_x.index("\n")
        passport_all += " " + entry_x[:newline_index]
    if ((entry_x == "\n") or (i == count)):
        total_passports += 1
        field_num =  0
        for x in valid_fields:
            if (passport_all.find(x) != -1): field_num += 1
            else: print("\033[31m\tMISSING ", x)
        if (field_num == 7): valid_count += 1
        #else: print("\033[31m", end='\r')
        print("Line ",i,"\tPassport#",total_passports," reads\t ", passport_all,"\033[0m")
        passport_all = ""
   
    i += 1

print(valid_count, " Total Valid Passports out of ", total_passports)


#close file, we're done with it
print("...Closing File")
inputfile.close() 