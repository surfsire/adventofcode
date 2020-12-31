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
print(groups)

letters = "abcdefghijklmnopqrstuvwxyz"
group_all = [0]
i = 1
while (i <= group_cnt):
    temp_txt = filecontent[groups[i-1]:groups[i]]
    temp_txt.pop(0)
    print(temp_txt)
    group_all.clear()
    for w in temp_txt:
        temp_string = w
        temp_string = temp_string[:temp_string.index("\n")]
        print(temp_string)
        for x in temp_string:
            group_all.append(x)
    print(group_all)
    for y in letters:
        if (group_all.count(y) > 0): group_yes += 1
    print(group_yes)
    #print(filecontent[groups[0]:groups[1]])
    i += 1


print("Sum of group yeses:",group_yes)


#close file, we're done with it
print("...Closing File")
inputfile.close() 