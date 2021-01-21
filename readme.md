## name-tool
a creatively named tool to suggest  names of a particular gender similar to an input name.

### usage

on linux you can just do:

`./sift.py [year] [gender] [input name]`

on other OSes you probably need to stick `python` or `python3` on the front of that.

[year] specifies a birth year. it is required for now. srry.

[gender] specifies a gender, and is 'm', 'f', or 'a'. A name that is >= 60% correllated with a particular sex (the dataset this uses only has 'M' and 'F'...) will be considered that gender for 'm' and 'f', and anything between 40% and 60% will be given for 'a'.

[input name] is a name you want the output to be similar to. The output is sorted by similarity to this name.

ex: `./sift.py 1969 f john`

