from selenium import webdriver
from selenium.webdriver.common.by import By

import os
class ByDemo():

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

            elementById = driver.find_element(By.ID, "name")

            if elementById is not None:
                print("We found an element by Id")
                print(elementById.text)

            elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

            if elementByXpath is not None:
                print("We found an element by XPATH")
                print(elementByXpath.text)

            elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")

            if elementByLinkText is not None:
                print("We found an element by Link Text")
                print(elementByLinkText.text)
        except:
            pass
        finally:
            driver.close()
            driver.quit()
ff = ByDemo()
ff.test()