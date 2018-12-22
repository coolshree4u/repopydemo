from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class RunFFTests():

    def test(self):
        # Instantiate FF Browser Command
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        firefox_capabilities['binary'] = '/home/shreeprasadpatil/Downloads/firefox/firefox'
        driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",capabilities= firefox_capabilities)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")
        driver.switch_to.default_content()
        driver.switch_to.parent_frame()

ff = RunFFTests()
ff.test()