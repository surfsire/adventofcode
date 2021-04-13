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
running_sum = 1
i = 1
while (i <= count):
    entry_x = filecontent[i]
    bag_name = entry_x[:(entry_x.index("bags contain")-1)]
    if (bag_name == bag_to_find):
        bags_in_bag = entry_x[(entry_x.index("bags contain")+13):]
        print(bags_in_bag)
        while (1):
            running_sum += int(bags_in_bag[0])
            total_bags.append(bags_in_bag[2:(bags_in_bag.index("bag")-1)])
            bags_in_bag = bags_in_bag[(bags_in_bag.index("bag")+3):]
            if (bags_in_bag[0] == "s"): bags_in_bag = bags_in_bag[1:]
            if (bags_in_bag[0] == ","): bags_in_bag = bags_in_bag[2:]
            print(running_sum,"\t",total_bags,"\t",bags_in_bag)
            if (bags_in_bag[0] == "."): break
    i += 1
    # if (entry_x.find(bag_to_find) != -1):
    #     bag_name = entry_x[:(entry_x.index("bags contain")-1)]
    #     if (bag_name != bag_to_find):
    #         total_bags.append(bag_name)
    #         print("Found",bag_to_find,"in \t",entry_x)
    #   i += 1



ii = 0 
prev_bag_tier = []
bags_accounted = []
while (ii < 1000):
    prev_bag_tier = total_bags 
    for x in prev_bag_tier:
        print("Searching for:",x,end=' ')
        y = 1
        while (y <= count): 
            entry_y = filecontent[y]
            bag_name = entry_y[:(entry_y.index("bags contain")-1)]
            #print("Checking...",bag_name)
            if (bag_name == x) :
                print("\033[32mFOUND!\033[0m")
                bags_in_bag = entry_y[(entry_y.index("bags contain")+13):]
                print(bags_in_bag)
                while (1):
                    if (bags_in_bag[0].isdigit()):
                        running_sum += int(bags_in_bag[0])
                        bag_to_add = bags_in_bag[2:(bags_in_bag.index("bag")-1)]
                        if not(bag_to_add in total_bags): total_bags.append(bag_to_add)
                    bags_in_bag = bags_in_bag[(bags_in_bag.index("bag")+3):]
                    if (bags_in_bag[0] == "s"): bags_in_bag = bags_in_bag[1:]
                    if (bags_in_bag[0] == ","): bags_in_bag = bags_in_bag[2:]
                    if (bags_in_bag[0] == "."): 
                        print(running_sum,"\t",total_bags,"\t",bags_in_bag)
                        break
            y += 1
    for items in total_bags :
        if not(items in bags_accounted) : bags_accounted.append(items)
    for items in prev_bag_tier :
        total_bags.remove(items)
        #print("Removed",items,"from list:\r\n",total_bags)
    if (total_bags == []): break
    ii += 1
#    i= 1
#     bags = []
#     print("=====================================\033[36m\r\n",find_bags,"\033[0m")
#     while (i <= count):
#         entry_x = filecontent[i]
#         for y in find_bags:
#             if (entry_x.find(y) != -1):
#                 bag_name = entry_x[:(entry_x.index("bags contain")-1)]
#                 if (bag_name != y):
#                     print("Found",y,"in \t",entry_x,end=" ")
#                     if (bag_name in total_bags) or (bag_name in bags):
#                         print("\033[31mAlready Counted\033[0m --",bag_name)
#                     else:
#                         print("\033[32mAdding to Count\033[0m --",bag_name)
#                         bags.append(bag_name)
#         i += 1
#     total_bags += bags
#     find_bags = bags
#     print("\033[34m",bags,"\033[0m\r\n=====================================")
#     if (bags == []): break
#     ii += 1

print(bags_accounted)
#print(total_bags)
print("Answer:", running_sum)


#close file, we're done with it
print("...Closing File")
inputfile.close() 