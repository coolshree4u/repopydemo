from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        driver = None
        try:
            driver = webdriver.Firefox()
            driver.maximize_window()
            # driver.get("https://letskodeit.teachable.com/pages/practice")
            driver.execute_script("window.location.href = 'https://letskodeit.teachable.com/pages/practice';")
#            driver.implicitly_wait(3)
            time.sleep(6)

            # element = driver.find_element(By.ID, "name")
            element = driver.execute_script("var element= document.getElementById('name'); element.innerHTML='test';")
            #element.send_keys("Test")
        except Exception as e:
            print(e)
            print('Inside exception')
        finally:
            driver.quit()

ff = JavaScriptExecution()
ff.test()