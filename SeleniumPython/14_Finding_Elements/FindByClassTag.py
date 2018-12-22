from selenium import webdriver
import os

class FindByClassTag():

    def test(self):
        driver=None
        try:
            baseUrl = "https://letskodeit.teachable.com/pages/practice"
            driverLocation = "/usr/local/bin/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation
            # Instantiate Chrome Browser Command
            driver = webdriver.Chrome(driverLocation)
            driver.maximize_window()
            driver.get(baseUrl)

            elementByClassName = driver.find_element_by_class_name("displayed-class")
            elementByClassName.send_keys("Testing The Element")

            if elementByClassName is not None:
                print("We found an element by Class Name")

            elementByTagName = driver.find_element_by_tag_name("h1")
            text = elementByTagName.text

            if elementByTagName is not None:
                print("We found an element by Tag Name and the text on element is: " + text)
        except:
            pass
        finally:
            driver.close()
            driver.quit()

ff = FindByClassTag()
ff.test()