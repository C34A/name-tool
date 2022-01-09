

from typing import Dict
from typing import Dict
from nameutils import *
import csv

def read_to_dict(out: Dict[str, NameStruct], file: str) -> None:
    try:
        file = open(file)
    except:
        print("unable to open", file)
        print("year input is likely invalid")
    csvreader = csv.reader(file, delimiter=',')

    for row in csvreader:
        name = row[0].lower()
        sex = row[1].lower()
        occurrences = int(row[2])
        if not name in out:
            # initialie this one
            out[name] = NameStruct(name)
        if sex == 'm':
            out[name].add_m(occurrences)
        elif sex == 'f':
            out[name].add_f(occurrences)
        else:
            print("unknown sex - " + name + ":" + sex + "!")
            # I don't think this dataset has anything except
            # M and F in it, but idk.

    file.close()