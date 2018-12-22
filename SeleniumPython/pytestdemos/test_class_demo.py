import pytest


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestClassDemo():

    def classSetup(self):
        self.abc=SomeClassToTest(10)

    def test_methodA(self):
        print("Runnning Method A")


    def test_methodB(self):
        print("Runnning Method B")