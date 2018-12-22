from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
class ElementState():

    def isEnabled(self):
        driver=None
        try:
            baseUrl = "http://www.google.com"
            cap=DesiredCapabilities.FIREFOX
            print(cap)
            driverLocation = "/usr/local/bin/geckodriver"
            os.environ["webdriver.gecko.driver"] = driverLocation
            # Instantiate Chrome Browser Command
            driver = webdriver.Firefox(capabilities=cap,executable_path= driverLocation)
            driver.maximize_window()
            driver.get(baseUrl)
            driver.implicitly_wait(3)

            e1 = driver.find_element_by_id("gs_htif0")
            e1State = e1.is_enabled() # True for enabled and False for disabled
            print("E1 is Enabled? -> " + str(e1State))

            e2 = driver.find_element_by_id("gs_taif0")
            e2State = e2.is_enabled()  # True for enabled and False for disabled
            print("E2 is Enabled? -> " + str(e2State))

            e3 = driver.find_element_by_id("lst-ib")
            e3State = e3.is_enabled()  # True for enabled and False for disabled
            print("E3 is Enabled? -> " + str(e3State))

            e3.send_keys("letskodeit")
        except Exception as e:
            print(e)
        finally:
            #driver.close()
            driver.quit()

e = ElementState()
e.isEnabled()