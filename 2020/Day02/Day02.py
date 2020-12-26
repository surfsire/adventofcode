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

#Entry pattern #-# x: pswd
valid_pswd = 0
x = 1
while (x <= count):
    entry_x = filecontent[x]
    min_char = int(entry_x[:entry_x.index("-")]) #pull first number, value before '-'
    max_char = int(entry_x[(entry_x.index("-")+1):entry_x.index(" ")]) #pull second number, value between '-' and first space
    req_char = entry_x[(entry_x.index(" ")+1):entry_x.index(":")] #pull required char, value between first space and ':'
    pswd = entry_x[(entry_x.index(": "))+2:] #pull password, remaining char after :
    char_count = int(pswd.count(req_char))
    if (min_char <= char_count <= max_char):
        print("\033[32m",x,"\t:", entry_x,"Min: ", min_char, "\tMax: ", max_char,"\tREQ: ", req_char,"\t Password: ",pswd,"\033[0m")
        valid_pswd += 1
    else: print("\033[31m",x,"\t:", entry_x,"Min: ", min_char, "\tMax: ", max_char,"\tREQ: ", req_char,"\t Password: ",pswd,"\033[0m")
    x += 1
    

print("There were ", valid_pswd, " valid passwords out of ", count)

#close file, we're done with it
print("...Closinging File")
inputfile.close() 