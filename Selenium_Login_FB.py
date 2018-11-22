from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


username = "shubhamrouth@gmail.com"
password = "Hellboy@26021991"

driver = webdriver.Ie("F:\Python\IEDriverServer.exe")
#driver = webdriver.Chrome("F:\Python\chromedriver.exe")
driver.get("https://ssl.comodo.com/articles/make-life-simple-with-an-automated-ssl-certificate-expiry-check.php")

try:
    
    time.sleep(5)

    #locate by link text
    element = driver.find_element_by_link_text("EV SSL")
    element.click()

    time.sleep(5)
    
    element = driver.find_element_by_link_text("EV Code Signing")
    element.click()

    time.sleep(4)
    driver.maximize_window()
    
    #screenshot
    element = driver.find_element_by_tag_name('body')
    element_png = element.screenshot_as_png
    with open("C:/Users/Admin/Desktop/TestData/screenshot1.jpg", "wb") as file:
        file.write(element_png)
    #driver.get_screenshot_as_file('C:/Users/Admin/Desktop/TestData/screenshot1.jpg')

    
finally:
    print("Text entered")

