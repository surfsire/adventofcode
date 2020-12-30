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
            byr = passport_all[(passport_all.index("byr:")+4):(passport_all.index("byr:")+4+4)]
            try: byr.isdigit()
            except: print ("\033[31m\tINVALID Birth Year (format)\t", byr)
            else:
                if ((byr.isdigit()) and (1920 <= int(byr) <= 2002)): field_num += 1
                else: print ("\033[31m\tINVALID Birth Year (range)\t", byr)

            iyr = passport_all[(passport_all.index("iyr:")+4):(passport_all.index("iyr:")+4+4)]
            try: (iyr.isdigit)
            except: print ("\033[31m\tINVALID Issue Year (format)\t", iyr)
            else:
                if ((iyr.isdigit) and (2010 <= int(iyr) <= 2020)): field_num += 1
                else: print ("\033[31m\tINVALID Issue Year (range)\t", iyr)

            eyr = passport_all[(passport_all.index("eyr:")+4):(passport_all.index("eyr:")+4+4)]
            try: eyr.isdigit()              
            except: ("\033[31m\tINVALID Expire Year (format)\t", eyr)
            else:
                if ((eyr.isdigit()) and (2020 <= int(eyr) <= 2030)): field_num += 1
                else: print ("\033[31m\tINVALID Expire Year\t", eyr)

            hgt = passport_all[(passport_all.index("hgt:")+4):(passport_all.index("hgt:")+4+5)]
            if ((hgt.find("cm") != -1) or (hgt.find("in") != -1)):
                if hgt[hgt.find("cm")-3:hgt.find("cm")].isdigit():
                    if (150 <= int(hgt[hgt.find("cm")-3:hgt.find("cm")]) <= 193): field_num += 1
                elif hgt[hgt.find("in")-2:hgt.find("in")].isdigit():
                    if (59 <= int(hgt[hgt.find("in")-2:hgt.find("in")]) <= 76): field_num += 1
                else: print ("\033[31m\tINVALID Height (range)\t", hgt)
            else: print ("\033[31m\tINVALID Height (format)\t\t", hgt)

            hcl = passport_all[(passport_all.index("hcl:")+4):(passport_all.index("hcl:")+4+7)]
            try:    int(hcl[hcl.index("#")+1:+hcl.index("#")+1+6],16)
            except: print ("\033[31m\tINVALID Hair Color\t", hcl)
            else:
                if (len(hcl) == 7) and (0x000000 <= int(hcl[hcl.find("#")+1:+hcl.find("#")+1+6],16) <= 0xFFFFFF): field_num += 1
                else: print ("\033[31m\tINVALID Hair Color (range)\t", hcl)
            
            ecl = passport_all[(passport_all.index("ecl:")+4):(passport_all.index("ecl:")+4+3)]
            ecl = ecl.lower()
            valid_ecl = ["amb","blu","brn","gry","grn","hzl","oth"]
            ecl_found = False
            for x in valid_ecl: 
                if (ecl == x): ecl_found = True
            if ecl_found: field_num += 1
            else: print ("\033[31m\tINVALID Eye Color\t", ecl)

            pid = passport_all[(passport_all.index("pid:")+4):(passport_all.index("pid:")+4+9)]
            pid.rstrip()
            if (len(pid) == 9) and (pid.isdigit()): field_num += 1
            else: print ("\033[31m\tINVALID PID\t\t", pid)
        
        if (field_num == 14): valid_count += 1
        else: print("\033[31m", end='\r')
        print("Line ",i,"\tPassport#",total_passports," Vaild count:", valid_count,"\t ", passport_all,"\033[0m")
        passport_all = ""
   
    i += 1

print(valid_count, " Total Valid Passports out of ", total_passports)


#close file, we're done with it
print("...Closing File")
inputfile.close() 