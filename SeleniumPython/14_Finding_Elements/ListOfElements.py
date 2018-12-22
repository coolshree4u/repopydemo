from selenium import webdriver
from selenium.webdriver.common.by import By
import os
class ListOfElements():

    def test(self):
        driver= None
        try:
            baseUrl = "https://letskodeit.teachable.com/pages/practice"
            driverLocation = "/usr/local/bin/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation
            # Instantiate Chrome Browser Command
            driver = webdriver.Chrome(driverLocation)
            driver.maximize_window()
            driver.get(baseUrl)

            elementListByClassName = driver.find_elements_by_class_name("inputs")
            length1 = len(elementListByClassName)

            if elementListByClassName is not None:
                print("ClassName -> Size of the list is: " + str(length1))
                for item in elementListByClassName:
                    print(item.text)

            elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
            length2 = len(elementListByTagName)

            if elementListByTagName is not None:
                print("TagName -> Size of the list is: " + str(length2))
                for item in elementListByTagName:
                    print(item.text)
        except:
            pass
        finally:
            driver.close()
            driver.quit()
ff = ListOfElements()
ff.test()