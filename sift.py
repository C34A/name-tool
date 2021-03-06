#!/usr/bin/python3

import sys
import csv

from nameutils import NameStruct

year = sys.argv[1] # a year, in YYYY format
input_gender = sys.argv[2].lower()
if input_gender != "m" and input_gender != "f" and input_gender != "n":
    print("this tool only uses 'm', 'f', or 'n' for input gender.")
    print("'m' for masculint, 'f' for feminint, 'n' for gender neutral.")
    print("names between 40% and 60% masculine/feminine are considered gender neutral")
    exit()

input_name = sys.argv[3] # a name (or whatever, it doesn't actually matter lol)

file = open("./namesdb/yob" + year + ".txt")
csvreader = csv.reader(file, delimiter=',')

names = {}

for row in csvreader:
    name = row[0].lower()
    sex = row[1].lower()
    occurrences = int(row[2])
    if not name in names:
        # initialie this one
        names[name] = NameStruct(name)
    if sex == 'm':
        names[name].add_m(occurrences)
    elif sex == 'f':
        names[name].add_f(occurrences)
    else:
        print("unknown sex - " + name + ":" + sex + "!")
        # I don't think this dataset has anything except
        # M and F in it, but idk.

file.close()

siftlist = []

for name in names.values():
    gen = name.get_gender() 
    # these could be or'd but i don't like long lines :P
    if input_gender == 'n' and gen > 0.4 and gen < 0.6:
        siftlist.append(name)
    if input_gender == 'm' and gen > 0.6:
        siftlist.append(name)
    if input_gender == 'f' and gen < 0.4:
        siftlist.append(name)

def similarity(name: NameStruct) -> float:
    return name.similarity(input_name)

# Change 100 here to how many you want
# You can switch reverse to False if you want the least similar
top_n = sorted(siftlist, key=similarity, reverse=False)[:100] 

for name in top_n:
    gender_float = name.get_gender()
    mf = "masculine" if gender_float > 0.5 else "feminine"
    mf_float = "{:.2f}".format((gender_float if gender_float > 0.5 else \
                                (1.0 - gender_float)) * 100.0)
    print(name.name + ": " + mf_float + "% " + mf + " (n=" + str(name.get_n()) + ")")
