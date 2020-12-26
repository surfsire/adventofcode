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
    pswd = entry_x[(entry_x.index(":"))+1:] #pull password, remaining char after ': '
    pswd = pswd.lstrip()
    
    # char_count = int(pswd.count(req_char))
    # if (min_char <= char_count <= max_char):
    if (((pswd[min_char-1] == req_char) or (pswd[max_char-1] == req_char)) and (pswd[min_char-1] != pswd[max_char-1])):
        print("\033[32m")
        valid_pswd += 1
    else: print("\033[31m")

    print(x,"\t", entry_x,"Min: ", min_char, " [",pswd[min_char-1],"]\tMax: ", max_char, "[", pswd[max_char-1],"]\tREQ: ", req_char,"\t Password: ",pswd,"\033[0m")
    x += 1

print("There were ", valid_pswd, " valid passwords out of ", count)

#close file, we're done with it
print("...Closinging File")
inputfile.close() 