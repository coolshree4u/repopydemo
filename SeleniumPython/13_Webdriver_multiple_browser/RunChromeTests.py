from selenium import webdriver
import os

class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "/usr/local/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")
        driver.maximize_window()
        driver.close()
        driver.quit()

ff = RunChromeTests()
ff.test()