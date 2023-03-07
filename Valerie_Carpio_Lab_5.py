from selenium import webdriver #This imports the webdriver from selenium to allow your code to navigate the website
from selenium.webdriver.chrome.service import Service #This imports Service from the driver through Chrome to let it start and stop Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #This imports the By locator, which lets selenium read and select common locators (ex: LINK_TEXT)
from selenium.webdriver.support.ui import WebDriverWait #This imports the WebDriverWait module to allow us to see what the webdriver does
from selenium.webdriver.support import expected_conditions as EC #This imports expected conditions as EC to be used to return True if elements are located

#Section 1: Code from Video Tutorial

PATH = Service("C: \Program Files (x86) \Google.exe") #This states the way (PATH) to reach the webdriver
driver = webdriver.Chrome(service = PATH) #This sets the driver = the webdriver within Chrome using the path to reach selenium

driver.get("https://www.techwithtim.net/") #This allows the driver to access the website we want to use

link = driver.find_element(By.LINK_TEXT, "Python Programming") #This causes the link to = the element found under the link_text "Python Programming" on the aforementioned site

try: #This gets selenium to the try the commands below
    element = WebDriverWait(driver, 10).until(  #This makes the element = to the webdriver running for 10 seconds, until a condition is met
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")) #This says the webdriver will run until the link_text "Beginner Python Tutorials" is found
    )
    element.click() #This then clicks the link_text "Beginner Python Tutorials"

    element = WebDriverWait(driver, 10).until(  #This makes the element = to the webdriver running for 10 seconds, until a condition is met
        EC.presence_of_element_located((By.ID, "sow-button-19310003")) #This says the webdriver will run until the ID "sow-button-19310003" is found
    )
    element.click() #This then clicks the link_text "Beginner Python Tutorials"

    driver.back() #This tells the driver to navigate back, to the previous page
    driver.back() #This tells the driver to navigate back, to the previous page
    driver.back() #This tells the driver to navigate back, to the previous page
    driver.forward() #This tells the driver to navigate forwards, to the page they just left
    driver.forward() #This tells the driver to navigate forwards, to the page they just left

except: #This creates an except for the above commands don't work when tried 
    driver.quit() #This causes the driver to quit

#Section 2:
from bs4 import BeautifulSoup
import requests
import html5lib
import csv
import pandas as pd
PATH = Service("C: \Program Files (x86) \Google.exe") 
driver = webdriver.Chrome(service = PATH) 

site = "https://www.wikipedia.org/"
cat_search = "https://en.wikipedia.org/wiki/Cat"
driver.get(site) 

url = driver.find_element(By.NAME, "search")
url.clear()
url.send_keys("Cats") #runs test in the search field
url.send_keys(Keys.RETURN) 

reqs = requests.get(cat_search)
content = reqs.text
soup = BeautifulSoup(content, "html.parser")

urls = []
for h in soup.find_all("figure"):
    a = h.find("a")
    try:
        if "href" in a.attrs: 
            url = a.get("href")
            urls.append(url)
    except:
        pass
    
for url in urls:
    print(url)