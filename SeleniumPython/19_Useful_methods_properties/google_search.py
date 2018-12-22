from selenium import webdriver
from selenium.webdriver.common.by import By as test
import time
driver=None
try:
    driver= webdriver.Firefox()
    driver.get(url="https://www.google.co.in/")
    searchBox=driver.find_element(test.CSS_SELECTOR,"input[title='Search']")
    searchBox.send_keys("test String")

    time.sleep(2)
    btnGoogleSearch=driver.find_element(test.CSS_SELECTOR,"input[type='button'][value='Google Search']")
    btnGoogleSearch.click()
    time.sleep(2)
    searchedKeyword=driver.find_element(test.CSS_SELECTOR,"input[title='Search']")
    #print(searchedKeyword.value_of_css_property("value"))

    list_links=driver.find_elements_by_css_selector("h3>a")
    count=0
    for links in list_links:
        count+=1
        if count==3:
            print(links.text)

except Exception as e:
    print(e)
finally:
    driver.quit()