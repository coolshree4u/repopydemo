from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import os


def test():
    driver = None
    try:
        baseUrl = "http://10.2.9.41/"
        driverLocation = "/usr/local/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='LOGIN_user']/..")


        #newElement=elementByXpath.find_element_by_xpath('..')
        attrs = driver.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
            elementByXpath)
        print(attrs)
    except NoSuchElementException:
        print(NoSuchElementException)
    finally:
        driver.close()
        driver.quit()

test()