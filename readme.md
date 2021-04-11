## name-tool
A creatively named tool to suggest names of a particular gender similar to an input name. Uses data from https://www.ssa.gov/oact/babynames/limits.html

### dependencies

This tool has the optional dependencies of  [phonetics](https://pypi.org/project/phonetics/) and [python-Levenshtein](https://pypi.org/project/python-Levenshtein/). These can be removed by deleting the erroneous imports and replacing the `NameStruct.similarity()` function with the `NameStruct.old_similarity` function (both in `nameutils.py`). Doing this may or may not produce worse results (both systems do a pretty mediocre job, honestly).

### usage

on linux you can just do:

`./sift.py [year] [gender] [input name]`

on other OSes you probably need to stick `python` or `python3` on the front of that.

[year] specifies a birth year, between 1880 and 2019. it is required for now. srry.

[gender] specifies a gender, and is 'm', 'f', or 'n'. A name that is >= 60% correllated with a particular sex (the dataset this uses only has 'M' and 'F'...) will be considered that gender for 'm' and 'f', and anything between 40% and 60% will be given for 'n'.

[input name] is a name you want the output to be similar to. The output is sorted by similarity to this name.

ex: `./sift.py 1969 f john`

### example output

```
$./sift.py 1969 f john
joan: 99.11% feminine (n=1580)
johna: 100.00% feminine (n=60)
jean: 89.00% feminine (n=2145)
jann: 100.00% feminine (n=34)
jan: 77.76% feminine (n=733)
jen: 100.00% feminine (n=6)
joann: 99.51% feminine (n=1643)
jonna: 100.00% feminine (n=125)
joana: 100.00% feminine (n=26)
jonni: 100.00% feminine (n=18)
joane: 100.00% feminine (n=9)
joani: 100.00% feminine (n=7)
joni: 98.25% feminine (n=343)
jona: 100.00% feminine (n=44)
johnna: 100.00% feminine (n=214)
...
```

