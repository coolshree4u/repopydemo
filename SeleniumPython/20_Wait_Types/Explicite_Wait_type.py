from HandyDemoo import HandyWrappers
class Explicite_Wait_Type:

    def __init__(self, driver):
        self.driver=driver
        self.hw= HandyWrappers()

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):

        element =None
        try:
            byType= self.hw.getByType(locatorType)
            print("Waiting for maximum :: "+str(timeout)+"  seconds for element to be clickable")

            print("Element appeared on the web page")
        except:
            print("Element  not appeared on the web page")
        return element