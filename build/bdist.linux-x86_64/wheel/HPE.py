"""
from __init__ import App
#m=App()
xyz=2
class abc:
    def abc(self):
        App.sim(self)

A=abc()
A.l=[1]
A.abc()

Below:

 > Required in order to run the documentation checker on this code.

 > The comment
     pragma: no cover
   means that this block of code will not be checked for unit test
   coverage by the `coverage` module.

"""
import unittest
import tests.test_
suite = unittest.TestLoader().loadTestsFromModule(test_)
unittest.TextTestRunner().run(suite)
