#!/usr/bin/env python3

#open file
from io import RawIOBase


print("Opening File...")
inputfile = open('input', 'r')

# **********************************
# Count Number of Lines in Input and Move to internal Array (leaves input file untouched)
numlines = inputfile.readline()
count = 0
filecontent = []
while numlines:
    filecontent.append(numlines) #int(float(numlines)))  #line items will have \n at end if not converted
    numlines = inputfile.readline()
    count += 1
print ("File has ", count, " lines")
#close file, we're done with it
print("\n...Closing File")
inputfile.close() 
# **********************************

# !!---------- PART I -----------!!
pulled_order = filecontent[0].split(",") #move randomly pulled list of numbers into its own array
long_list = []
answ1 = 0
answ2 = 0

BINGO = ["9999","9999","9999","9999","9999"]
BINGO_Cards = []
Cards_Left = 100

for card in range(0,100,1): #100 cards
    BINGO_Cards.append(int(card + 1))

for x in range(1,count): #Scan Each Line of Input (skipping first lines)
    #BINGO cards are 5x5, 6 rows with white space
    temp_row = filecontent[x].split()
    for i in temp_row:
        if (i != '\n'): long_list.append(int(float(i)))
cards_nomod = long_list.copy()
print("\nRandom PULL=",end='')
for pulled in pulled_order:
    print(" ",int(float(pulled)),end="")
    count_index = 0
    # MARK OFF PULLED NUMBERS
    for ii in long_list:
        if (ii) == int(float(pulled)):
            long_list[count_index] = "9999"
        count_index += 1
    for card in range(0,2500,25): #100 cards, 25 numbers each
        current_card = long_list[card:card+25]
        for row in range(0,25,5):
            column = []
            for col in range(0,5,1):
                column.append(current_card[int(row/5)+col*5])
            if ((current_card[row:row+5] == BINGO) or (column == BINGO)):
                
                if (len(BINGO_Cards) == 100):
                    print ("\n\n\033[0;33m!!!! === FIRST BINGO === !!!!\033[0m")
                    if (current_card[row:row+5] == BINGO): print ("     Card:",int(card/25)+1," Row:",int(row/5)+1,"\n")
                    if (column == BINGO): print("     Card:",int(card/25)+1," Column:",int(row/5)+1,"\n")
                    for r in range(0,25,5):
                        print (cards_nomod[card+r:card+r+5])
                    print ("\n\033[0;34m !=== Calculating First Answer ===! \033[0m")
                    print ("Adding:", end ='')
                    for sum in range(0,25,1):
                        if (current_card[sum] != "9999") :
                            print (",",current_card[sum],end='')
                            answ1 += current_card[sum]
                    print ("= ",answ1)
                    answ1 *= int(float(pulled))
                    print("Multiply by",pulled,"=  \033[34m",answ1,"\033[0m\n")
                    print("Continue Random PULLs... ",end='')
                
                if (BINGO_Cards.count(int(card/25)+1) > 0): BINGO_Cards.remove(int(card/25)+1)
                
                if (len(BINGO_Cards) == 0):
                    print ("\n\n\033[0;33m!!!! === LAST BINGO === !!!!\033[0m\n   Card:",int(card/25)+1," Row:",int(row/5)+1,"\n")
                    for r in range(0,25,5):
                        print (cards_nomod[card+r:card+r+5])
                    print ("\n\033[0;34m !=== Calculating Second Answer ===! \033[0m")
                    print ("Adding:", end ='')
                    for sum in range(0,25,1):
                        if (current_card[sum] != "9999") :
                            print (" ",current_card[sum],end='')
                            answ2 += current_card[sum]
                    print ("= ",answ2)
                    answ2 *= int(float(pulled))
                    print("Multiply by",pulled,"=  \033[34m",answ2,"\033[0m\n")
                    exit()