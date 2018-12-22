from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import os
class FindByIdName():

    def test(self):
        driver=None
        try:
            baseUrl = "https://letskodeit.teachable.com/pages/practice"
            driverLocation = "/usr/local/bin/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation
            # Instantiate Chrome Browser Command
            driver = webdriver.Chrome(driverLocation)
            driver.get(baseUrl)
            elementById = driver.find_element_by_id("name")

            if elementById is not None:
                print("We found an element by Id")

            elementByName = driver.find_element_by_name("show-hide")

            if elementByName is not None:
                print("We found an element by Name")

            driver.get("https://www.yahoo.com/")
            # This one should fail because the Id is not static
            # Exception thrown: NoSuchElementException
            driver.find_element_by_id("yui_3_18_0_4_1463100170626_1148")
        except NoSuchElementException:
            print(NoSuchElementException)
        finally:
            driver.close()
            driver.quit()
ff = FindByIdName()
ff.test()