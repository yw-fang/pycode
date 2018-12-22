# IMPORTANT NOTES

You may find that requirements.txt looks duplicated to install_requires in setup.py.
However, as far as I know (I google it!), they have different functionalities.
If we publish the code on PyPI, then only the install_requires in the setup.py will
be installed, and that ini the requirements.txt will not be installed.
Hence, the difference is that setup.py is used for distributing our package,
and if we want to document exactly which packages should be installed for
a testing or development venv, put them in a requirements.txt file.
In an advanced way, we can directly use requirements.txt in the setup.py in this way
"""
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='rockstar',
    version=version,
    install_requires=requirements
    )
    
In this way, we can only maintain the requirements.txt file. However,
for the time-being, I think maintaining these two files is better because
some times the package for testing in the requirements.txt are actually not
necessary for installation of the main code.   
    
[Reference](https://www.reddit.com/r/Python/comments/3uzl2a/setuppy_requirementstxt_or_a_combination/)
