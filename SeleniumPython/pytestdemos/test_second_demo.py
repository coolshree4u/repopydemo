import pytest

@pytest.yield_fixture()
def setUp():
    print("Running demo1 setUp")
    yield
    print("Running demo1 tearDown")

def test_demo1_methodA(setUp):
    print("Running demo1 method A")

def test_demo1_methodB(setUp):
    print("Running demo1 method B")