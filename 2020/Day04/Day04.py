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
            index_feild = passport_all.find(x)
            if (index_feild != -1): field_num += 1
            else: print("\033[31m\tMISSING ", x)
        if (field_num == 7):            
            passport_array = passport_all.split(" ")
            passport_array.sort() # sort list alphabetical
            if len(passport_array) == 9: passport_array.pop(2)
            #print(passport_array)
            
            byr = passport_array[1]
            byr = byr[4:]
            try: int(byr)
            except: print("\033[35m\tINVALD Birth Year (Format)\t", byr)
            else:
                 if (1920 <= int(byr) <= 2002): field_num += 1
                 else: print("\033[31m\tINVALD Birth Year (Range)\t", byr)
                        
            ecl = passport_array[2]
            ecl = ecl[4:]
            colors = ["amb","blu","brn","gry","grn","hzl","oth"]
            ecl_invalid = True
            if (len(ecl) == 3):
                for x in colors:
                    if (ecl.find(x) != -1):
                        field_num += 1
                        ecl_invalid = False
                if (ecl_invalid): print("\033[31m\tINVALD Eye Color\t\t",ecl)
            else: print("\033[35m\tINVALD Eye Color (Format)\t", ecl)
            
            eyr = passport_array[3]
            eyr = eyr[4:]
            try: int(eyr)
            except: print("\033[35m\tINVALD Expiration Year (Format)\t", eyr)
            else:
                 if (2020 <= int(eyr) <= 2030): field_num += 1
                 else: print("\033[31m\tINVALD Expiration Year (Range)\t", eyr)

            hcl = passport_array[4]
            hcl = hcl[5:]
            try: int(hcl,16)
            except: print("\033[35m\tINVALD Hair Color (Format)\t", hcl)
            else:
                if (len(hcl) == 6) and (0x000000 <= int(hcl,16) <= 0xFFFFFF): field_num += 1
                else: print("\033[31m\tINVALD Hair Color (Range)\t", hcl) 

            hgt = passport_array[5]
            hgt = hgt[4:]
            if (hgt.find("cm") != -1):
                hgt = hgt[:hgt.index("cm")]
                try: int(hgt)
                except: print("\033[35m\tINVALD Height (Format)\t\t", hgt)
                else:
                    if (150 <= int(hgt) <= 193): field_num += 1
                    else: print("\033[31m\tINVALD Height (Range)\t\t", hgt) 
            elif (hgt.find("in") != -1):
                hgt = hgt[:hgt.index("in")]
                try: int(hgt)
                except: print("\033[35m\tINVALD Height (Format)\t\t", hgt)
                else:
                    if (59 <= int(hgt) <= 76): field_num += 1
                    else: print("\033[31m\tINVALD Height (Range)\t\t", hgt) 
            else: print("\033[35m\tINVALD Height (Format)\t\t", hgt)

            iyr = passport_array[6]
            iyr = iyr[4:]
            try: int(iyr)
            except: print("\033[35m\tINVALD Issue Year (Format)\t", iyr)
            else:
                 if (2010 <= int(iyr) <= 2020): field_num += 1
                 else: print("\033[31m\tINVALD Issue Year (Range)\t", iyr)

            pid = passport_array[7]
            pid = pid[4:]
            try: int(pid)
            except: print("\033[35m\tINVALD ID (Format)\t\t", pid)
            else:
                 if (len(pid) == 9 ): field_num += 1
                 else: print("\033[31m\tINVALD ID (Range)\t\t", pid)

        if (field_num == 14): valid_count += 1
        else: print("\033[31m", end='\r')
        print("Line ",i,"\tPassport#",total_passports," Vaild count:", valid_count,"\t ", passport_all,"\033[0m")
        passport_all = ""
   
    i += 1

print(valid_count, " Total Valid Passports out of ", total_passports)


#close file, we're done with it
print("...Closing File")
inputfile.close() 