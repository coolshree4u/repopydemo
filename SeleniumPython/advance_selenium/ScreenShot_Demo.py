from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        driver = None
        try:
            baseUrl = "https://letskodeit.teachable.com/"
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(baseUrl)
            driver.implicitly_wait(3)

            driver.find_element(By.LINK_TEXT, "Login").click()
            driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
            driver.find_element(By.ID, "user_password").send_keys("abc")
            driver.find_element(By.NAME, "commit").click()
            destinationFileName = "test.png" # Mac
            # destinationFileName = "C:\\atomar\\Desktop" -> Windows

            try:
                driver.save_screenshot(destinationFileName)
                print("Screenshot saved to directory --> :: " + destinationFileName)
            except NotADirectoryError:
                print("Not a directory issue")
        except:
            print('Inside exception')
        finally:
            driver.quit()

ff = Screenshots()
ff.test()