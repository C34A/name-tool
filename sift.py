#!/usr/bin/python3

import argparse
import sifthelper

from nameutils import NameStruct

parser = argparse.ArgumentParser(description="finds similar names")
parser.add_argument("from_", metavar="YYYY", type=int,
                    help="start year")
parser.add_argument("to", metavar="YYYY", type=int,
                    help="end year")
parser.add_argument("gender", metavar="gender", type=str,
                    help="m, f, or n", choices=["m", "f", "n"])
parser.add_argument("name", metavar="name", type=str,
                    help="input name")
parser.add_argument("-n", metavar="num", type=int, default=100,
                    help="how many results to display (default 100)")
parser.add_argument("--different", action="store_true",
                    help="invert the results to find most different names")

args = parser.parse_args()

yearfrom = args.from_
if not yearfrom in range(1880, 2020):
    print("invalid year:", yearfrom)
    print("must be between 1880 and 2019 (inclusive)")
    exit()
yearto = args.to
if not yearto in range(1880, 2020):
    print("invalid year:", yearto)
    print("must be between 1880 and 2019 (inclusive)")

input_gender = args.gender
if input_gender != "m" and input_gender != "f" and input_gender != "n":
    print("this tool only uses 'm', 'f', or 'n' for input gender.")
    print("'m' for masculint, 'f' for feminint, 'n' for gender neutral.")
    print("names between 40% and 60% masculine/feminine are considered gender neutral")
    # print(f"input: {input_gender} t {type(input_gender)}")
    exit()

input_name = args.name # a name (or whatever, it doesn't actually matter lol)

names = {}

for y in range(yearfrom, yearto+1):
    sifthelper.read_to_dict(names, "./namesdb/yob" + str(y) + ".txt")

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
top_n = sorted(siftlist, key=similarity, reverse=args.different)[:args.n] 

for name in top_n:
    gender_float = name.get_gender()
    mf = "masculine" if gender_float > 0.5 else "feminine"
    mf_float = "{:.2f}".format((gender_float if gender_float > 0.5 else \
                                (1.0 - gender_float)) * 100.0)
    print(name.name + ": " + mf_float + "% " + mf + " (n=" + str(name.get_n()) + ")")
