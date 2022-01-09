## name-tool
A creatively named tool to suggest names of a particular gender similar to an input name. Uses data from https://www.ssa.gov/oact/babynames/limits.html

### dependencies

This tool has the optional dependencies of  [phonetics](https://pypi.org/project/phonetics/) and [python-Levenshtein](https://pypi.org/project/python-Levenshtein/). It can handle them being missing, but the results are likely to be much worse.
### usage

on linux you can just do:

`./sift.py [from] [to] [gender] [input name]`

on other OSes you probably need to stick `python` or `python3` on the front of that.

`[from]` and `[to]` specify a birth year range, between 1880 and 2019. it is required for now. Use the same number twice to specify only one year.

`[gender]` specifies a gender, and is 'm', 'f', or 'n'. A name that is >= 60% correllated with a particular sex (the dataset this uses only has 'M' and 'F'...) will be considered that gender for 'm' and 'f', and anything between 40% and 60% will be given for 'n'.

`[input name]` is a name you want the output to be similar to. The output is sorted by similarity to this name.

ex: `./sift.py 1960 1980 f john`

more options can be displayed using `./sift.py -h`

### example output

```
$./sift.py 1960 1980 f john -n 10
joan: 99.14% feminine (n=43960)
johna: 100.00% feminine (n=1138)
johni: 100.00% feminine (n=65)
jean: 91.99% feminine (n=53257)
jann: 96.47% feminine (n=652)
jenn: 100.00% feminine (n=10)
jan: 81.00% feminine (n=19889)
jen: 100.00% feminine (n=139)
joann: 99.63% feminine (n=35428)
jonna: 100.00% feminine (n=2595)
```

