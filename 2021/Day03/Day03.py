#!/usr/bin/env python3

#open file
print("Opening File...")
inputfile = open('input', 'r')

#count lines
numlines = inputfile.readline()
count = 0
filecontent = [0]
while numlines:
    filecontent.append(numlines) #int(float(numlines)))
    numlines = inputfile.readline()
    count += 1
print ("File has ", count, " lines")

#Start Scan of Each Line - Part 1
gam01 = 0 #Gamma Rate [Part of Power Consumption - Part 1]
eps01 = 0 #Epsilon Rate [Part of Power Consumption - Part 1]
for bit in range(0, 12):
    zer_bit = 0 #number of 0s in column 
    one_bit = 0 #number of 1 in column
    for x in range(1, count):
        entry_x = str(filecontent[x])
        entry_bit = entry_x[bit]
        if (entry_bit == '1'): one_bit += 1
        if (entry_bit == '0'): zer_bit += 1
    if (one_bit > zer_bit): 
        #print("More 1s than 0s in column ",bit,"\t\033[35mGAMMA\033[0m   increased by",2**(11-bit))
        gam01 += 2**(11-bit)
    if (zer_bit > one_bit): 
        #print("More 1s than 0s in column ",bit,"\t\033[35mEPSILON\033[0m increased by",2**(11-bit),"\033[0m")
        eps01 += 2**(11-bit)

#Start Scan of Each Line - Part 2
O2gen = filecontent[1:] #Oxygen Generator Rating [Part of Life Support Rating - Part 2]
CO2scrub = filecontent[1:] #Carbon DiOxide Scrubber Rating [Part of Life Support Rating - Part 2]
for bit in range(0, 12):
    zer_bit = 0 #number of 0s in column 
    one_bit = 0 #number of 1 in column
    O2gen_temp = []
    if len(O2gen) > 1:
        for x in range(len(O2gen)):
            entry_x = str(O2gen[x])
            entry_bit = entry_x[bit]
            if (entry_bit == '1'): one_bit += 1
            if (entry_bit == '0'): zer_bit += 1
        if (one_bit >= zer_bit): 
            for x in range(len(O2gen)):
                entry_x = str(O2gen[x])
                entry_bit = entry_x[bit]
                if (entry_bit == '1'): O2gen_temp.append(entry_x)
        elif (one_bit < zer_bit): 
            for x in range(len(O2gen)):
                entry_x = str(O2gen[x])
                entry_bit = entry_x[bit]
                if (entry_bit == '0'): O2gen_temp.append(entry_x)
        O2gen = O2gen_temp
print(O2gen)

for bit in range(0, 12):
    zer_bit = 0 #number of 0s in column 
    one_bit = 0 #number of 1 in column
    CO2scrub_temp = []
    if len(CO2scrub) > 1 :
        for x in range(len(CO2scrub)):
            entry_x = str(CO2scrub[x])
            entry_bit = entry_x[bit]
            if (entry_bit == '1'): one_bit += 1
            if (entry_bit == '0'): zer_bit += 1
        if (one_bit < zer_bit): 
            for x in range(len(CO2scrub)):
                entry_x = str(CO2scrub[x])
                entry_bit = entry_x[bit]
                if (entry_bit == '1'): CO2scrub_temp.append(entry_x)
        elif (one_bit >= zer_bit): 
            for x in range(len(CO2scrub)): #scrub rows that have 0s
                entry_x = str(CO2scrub[x])
                entry_bit = entry_x[bit]
                if (entry_bit == '0'): CO2scrub_temp.append(entry_x)
        CO2scrub = CO2scrub_temp
print(CO2scrub)

print("\n\033[0;34m !=== ANSWERS ===! \033[0m")
print("PART I  \tGamma Rate: \033[0;33m",gam01,"\033[0m Epsilon Rate: \033[0;33m",eps01,"\033[0m -- Product: \033[0;32m",gam01 * eps01,"\033[0m") #Puzzle Answer #1
print("PART II \tOxygen Generator Rating: \033[0;33m",int(float(O2gen[0])),"\033[0m CO2 Scrubber Rating: \033[0;33m",int(float(CO2scrub[0])),"\033[0m -- Product: \033[0;32m",int(O2gen[0],2) * int(CO2scrub[0],2),"\033[0m") #Puzzle Answer #2

#close file, we're done with it
print("\n...Closing File")
inputfile.close() 
