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

bag_to_find = "shiny gold"

total_bags = []
i = 1
while (i <= count):
    entry_x = filecontent[i]
    if (entry_x.find(bag_to_find) != -1):
        bag_name = entry_x[:(entry_x.index("bags contain")-1)]
        if (bag_name != bag_to_find):
            total_bags.append(bag_name)
            print("Found",bag_to_find,"in \t",entry_x)
    i += 1

find_bags = total_bags

ii =0 
while (ii < 100):
    i= 1
    bags = []
    print("=====================================\033[36m\r\n",find_bags,"\033[0m")
    while (i <= count):
        entry_x = filecontent[i]
        for y in find_bags:
            if (entry_x.find(y) != -1):
                bag_name = entry_x[:(entry_x.index("bags contain")-1)]
                if (bag_name != y):
                    print("Found",y,"in \t",entry_x,end=" ")
                    if (bag_name in total_bags) or (bag_name in bags):
                        print("\033[31mAlready Counted\033[0m --",bag_name)
                    else:
                        print("\033[32mAdding to Count\033[0m --",bag_name)
                        bags.append(bag_name)
        i += 1
    total_bags += bags
    find_bags = bags
    print("\033[34m",bags,"\033[0m\r\n=====================================")
    if (bags == []): break
    ii += 1


bag_count = 0
for x in total_bags:
    bag_count += 1


#print(total_bags)
print("Answer:", bag_count)


#close file, we're done with it
print("...Closing File")
inputfile.close() 