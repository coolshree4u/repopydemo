# import pytest
#
# @pytest.yield_fixture()
# def setUp():
#     print("Running method level setUp")
#     yield
#     print("Running method level tearDown")
#
#
# @pytest.yield_fixture(scope="module")
# def oneTimeSetUp():
#     print("Running conftest demo one time setUp")
#     yield
#     print("Running conftest demo one time tearDown")



# conftest.py for testing parameters
# import pytest
#
# @pytest.yield_fixture()
# def setUp():
#     print("Running method level setUp")
#     yield
#     print("Running method level tearDown")
#
#
# @pytest.yield_fixture(scope="class")
# def oneTimeSetUp(browser,osType):
#     print("Running one time setUp")
#     if browser == 'firefox':
#         print("Running tests on FF")
#     else:
#         print("Running tests on chrome")
#     yield
#     print("Running one time tearDown")
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--osType", help="Type of operating system")
#
# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope="session")
# def osType(request):
#     return request.config.getoption("--osType")

#html generate report
import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'firefox':
        value = 10
        print("Running tests on FF")
    else:
        value = 20
        print("Running tests on chrome")

    if request.cls is not None:
        request.cls.value = value

    yield value
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--html")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


@pytest.fixture(scope="session")
def html(request):
    return request.config.getoption("--html")