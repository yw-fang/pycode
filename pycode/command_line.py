import pycode

def main():
    print(pycode.greetings()+'entry point functionality')


"""
We can register this main function in setup.py by

setup(
    ...
    entry_points = {
        'console_scripts': ['print_greetings_entry=pycode.command_line:main'],
    }
    ...
)

To use it:

Install pycode, and run in the terminal:

print_greetings_entry
"""