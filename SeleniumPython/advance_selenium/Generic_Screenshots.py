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
            self.takeScreenshot(driver)
        except:
            print('Inside exception')
        finally:
            driver.quit()


    def takeScreenshot(self, driver):
        """
        Takes screenshot of the current open web page
        :param driver
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"

        try:
            driver.save_screenshot(fileName)
            print("Screenshot saved to directory --> :: " + fileName)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()