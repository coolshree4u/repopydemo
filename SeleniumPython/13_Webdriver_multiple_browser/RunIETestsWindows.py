from selenium import webdriver
import os

class RunIETestsWindows():

    def test(self):
        driverLocation = "path to IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverLocation
        driver = webdriver.Ie(driverLocation)
        driver.get("http://www.letskodeit.com")

ieTest = RunIETestsWindows()
ieTest.test()