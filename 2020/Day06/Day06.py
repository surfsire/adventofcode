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

groups = [0]
group_cnt = 1
group_yes = 0
i = 1
while (i <= count):
    entry_x = filecontent[i]
    if (entry_x == ("\n")):
        groups.append(i)
        group_cnt += 1
    i += 1
groups.append(count+1)
print("There are",group_cnt,"groups")

letters = "abcdefghijklmnopqrstuvwxyz"
group_all = [0]
i = 1
while (i <= group_cnt):
    temp_list = filecontent[groups[i-1]:groups[i]]
    temp_list.pop(0)
    temp_list_count = 0
    for w in temp_list:
        temp_list_count += 1
    print("Group",i,"\t",temp_list_count,"Sets\t",temp_list)
    letters = [0]
    letters.clear()
    for x in temp_list[0]:
        if (x != "\n"): letters.append(x)
    ii = 0
    removal = [0]
    removal.clear()
    while (ii <= (temp_list_count-1)):
        print("\r\n================\r\nChecking next set...",temp_list[ii])
        for x in letters:
            print("Checking for...",x,end=' ')
            if (temp_list[ii].count(x) == 0):
                print("\033[31mNot found!\033[0m\t",end=' ')
                if (removal.count(x) == 0): removal.append(x)
                print(removal)
            else:
                print("\033[34m Found!   \033[0m")
        ii += 1
    for y in removal:
        letters.remove(y)
    current_yeses = 0
    for z in letters:
        current_yeses += 1
    group_yes += current_yeses
    print("        Common",current_yeses,"\t",letters,"\r\n    Total now",group_yes,"\t=================================================================\r\n")
    i += 1


print("Sum of group yeses:",group_yes)


#close file, we're done with it
print("...Closing File")
inputfile.close() 