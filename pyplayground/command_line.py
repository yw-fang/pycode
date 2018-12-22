import pyplayground

def main():
    print(pyplayground.greetings()+'entry point functionality')


"""
We can register this main function in setup.py by

setup(
    ...
    entry_points = {
        'console_scripts': ['print_greetings_entry=pyplayground.command_line:main'],
    }
    ...
)

To use it:

Install pyplayground, and run in the terminal:

print_greetings_entry
"""