from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        driver = None
        try:
            baseUrl = "http://www.expedia.com"
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(baseUrl)
            driver.implicitly_wait(3)

            # Click flights tab
            driver.find_element_by_id("tab-flight-tab").click()
            # Find departing field
            departingField = driver.find_element_by_id("flight-departing")
            # Click departing field
            departingField.click()
            # Find the date to be selected
            # Expedia website has changed the DOM after the lecture was made
            # Updated new xpath
            dateToSelect = driver.find_element(By.XPATH,
                                               "(//div[@class='datepicker-cal-month'])[1]//button[text()='30']")
            # Click the date
            dateToSelect.click()

            time.sleep(3)
        except:
            print('Inside exception')
        finally:
            driver.quit()

    def test2(self):
        driver = None
        try:
            baseUrl = "http://www.expedia.com"
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(baseUrl)
            driver.implicitly_wait(3)

            # Click flights tab
            driver.find_element(By.XPATH, "//button[@id='tab-package-tab-hp']//span[@class='tab-label']").click()
            # Find departing field
            departingField = driver.find_element_by_id("package-departing-hp-package")
            # Click departing field
            departingField.click()
            # Expedia website has changed the DOM after the lecture was made
            # Updated new xpath
            calMonth = driver.find_element(By.XPATH, "(//div[@class='datepicker-cal'])[1]")
            allValidDates = calMonth.find_elements(By.TAG_NAME, "button")

            time.sleep(2)

            for date in allValidDates:
                if date.text == "30":
                    date.click()
                    break
        except:
            print('Inside exception')
        finally:
            driver.quit()
ff = CalendarSelection()
ff.test2()