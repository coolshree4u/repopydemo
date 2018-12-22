from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=None

try:
    driver=webdriver.Firefox()
    driver.get("http://leap.parkar.consulting/login")
    time.sleep(3)

    username=driver.find_element(By.CSS_SELECTOR,"input[id='email']")
    print(username)
    username.send_keys("smaheshwari@parkar.consulting")
    time.sleep(2)

    password=driver.find_element(By.NAME,"password")
    print(password)
    password.send_keys("abcdefg")

    loginBtn=driver.find_element_by_css_selector("input[value = 'Log in']")
    loginBtn.click()

    time.sleep(2)
    verify_result=driver.find_element_by_css_selector("span[class='help-block']")
    print(verify_result.text)

except:
    pass
finally:
    driver.quit()