from selenium import webdriver
from selenium.webdriver.common.by import By

driver=None
try:
    driver=webdriver.Firefox()
    driver.get("https://www.facebook.com/")
    elements = driver.find_elements(By.CSS_SELECTOR,"img")

    for element in elements:
        attrs = driver.execute_script(
        'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
        element)
        print(attrs)

    icon_dict = {'wrench': 'edit.png',
                 'reports': 'reports.png',
                 'interface': 'if.png',
                 'event off': 'event_off.png',
                 'printer': 'printer.png',
                 'ticket': 'ticketing.png',
                 'asset off': 'asset_off.png',
                 'calendar': 'cal.png',
                 'imageDemo':'hsts-pixel.gif'
                 }
    icon_type='imageDemo'
    image=icon_dict[icon_type]
    print([icon.get_attribute('src') for icon in elements if image in icon.get_attribute("src")][0])
except Exception as e:
    print(e)
finally:
    driver.close()