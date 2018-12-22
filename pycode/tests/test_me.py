from unittest import TestCase
import pycode
# The testme.py file is my first test file.
# Although it’s overkill for now, we’ll use a
# unittest.TestCase subclass to provide infrastructure for later development.

"""
Test method 1
to run this test
$ cd tests/
$ pip install nose
$ nosetests
"""

class TestPlaygroud(TestCase):
    def test_is_string(self):
        mystrings = pycode.greetings()
        self.assertTrue(isinstance(mystrings, str))
        # self.assertTrue(isinstance(mystrings, basestring)) # for python 2.7


"""
Test method 2

To integrate above with our setup.py,
and ensure that Nose is installed when we run the tests, we’ll add a few lines to setup():

setup(
    ...
    test_suite='nose.collector',
    tests_require=['nose'],
)

To run this tests, we can do by:

$ python setup.py test
"""
