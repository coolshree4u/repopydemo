from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class ClickAndSendKeys():

    def test(self):
        driver=None
        try:
            baseUrl = "https://letskodeit.teachable.com"
            driverLocation = "/usr/local/bin/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation
            # Instantiate Chrome Browser Command
            driver = webdriver.Chrome(driverLocation)
            driver.maximize_window()
            driver.get(baseUrl)
            driver.implicitly_wait(10)

            loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
            loginLink.click()

            emailField = driver.find_element(By.ID, "user_email")
            emailField.send_keys("test")

            passwordField = driver.find_element(By.ID, "user_password")
            passwordField.send_keys("test")

            time.sleep(3)

            emailField.clear()

            time.sleep(3)

            emailField.send_keys("test")
        except:
            print("Inside error")
        finally:
            driver.close()
            driver.quit()



ff = ClickAndSendKeys()
ff.test()