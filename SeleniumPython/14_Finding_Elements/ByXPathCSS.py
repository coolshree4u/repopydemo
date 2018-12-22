from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import os
class FindByXPathCSS():

    def test(self):
        driver=None
        try:
            baseUrl = "https://letskodeit.teachable.com/pages/practice"
            driverLocation = "/usr/local/bin/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation
            # Instantiate Chrome Browser Command
            driver = webdriver.Chrome(driverLocation)
            driver.get(baseUrl)
            elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

            if elementByXpath is not None:
                print("We found an element by XPATH")

            elementByCss = driver.find_element_by_css_selector("div[class$='course-description']>h1")

            if elementByCss is not None:
                print("We found an element by CSS")
                print(elementByCss.text)
        except NoSuchElementException:
            print(NoSuchElementException)
        finally:
            driver.close()
            driver.quit()
ff = FindByXPathCSS()
ff.test()