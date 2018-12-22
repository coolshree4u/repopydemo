import unittest
from SeleniumPython.unittestdemo.FirstUnitTestDemo import TestCaseDemo1
from SeleniumPython.unittestdemo.Before_After_Class import TestCaseDemo2

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)