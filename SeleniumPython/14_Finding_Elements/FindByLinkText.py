from selenium import webdriver
import os

class FindByLinkText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driverLocation = "/usr/local/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")
            print(elementByLinkText.text)

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link Text")
            print(elementByPartialLinkText.text)
        driver.close()
        driver.quit()
ff = FindByLinkText()
ff.test()