#!/usr/bin/env python
import pycode

words = pycode.greetings()
askyou = '\n How are you?'
print(words+askyou)

"""
To use this script:
Firstly, install this pycode;
Secondly, just run 'print_greetings.py' in any terminal supporting python 3.

Note 1:

we can declare the script in setup() like this:

setup(
    ...
    scripts=['bin/funniest-joke'],
    ...
)

so that setuptools will copy the script to our PATH and make it
available in general use after installing our code.

Actually, we can use any other computer languages to write scripts
including bash shell because scripts here is generalizable
to non-python scripts.

Ref: https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html


Note 2:

Why do we need "#!/usr/bin/env python"?

Because /usr/bin/env can interpret your $PATH, which makes scripts more portable.
See Ref: 
https://unix.stackexchange.com/questions/29608/why-is-it-better-to-use-usr-bin-env-name-instead-of-path-to-name-as-my
"""