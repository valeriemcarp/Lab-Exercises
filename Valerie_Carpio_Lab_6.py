from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import requests, csv
from bs4 import BeautifulSoup
import pandas 
import time 

PATH = Service("C:\Program Files (x86) \Google.exe")
driver = webdriver.Chrome(service = PATH)
actions = ActionChains(driver)
site = "https://www.binghamton-ny.gov/home"
driver.get(site)

menu = driver.find_element(By.XPATH, "//*[@id='dropdownrootitem3']/a")
submenu = driver.find_element(By.XPATH, "//*[@id='dropdownrootitem3']/div/div/ul[1]/li/a")

actions.move_to_element(menu)
time.sleep(2)
actions.click(menu)
time.sleep(2)
actions.move_to_element(submenu)
time.sleep(2)
actions.click(submenu)
time.sleep(2)
actions.perform()

try:
    main = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".sidenav_expanded.sidenav_haschildren.sidenav_current"))
    )
    for i in driver.find_elements(By.CSS_SELECTOR, ".sidenav_expanded.sidenav_haschildren.sidenav_current"):
        civil = i.find_element(By.LINK_TEXT,"https://www.binghamton-ny.gov/government/departments/personnel-civil-service").click
        employment = i.find_element(By.LINK_TEXT, "https://www.binghamton-ny.gov/government/departments/personnel-civil-service/employment").click
except NoSuchElementException:
    pass
finally:
    driver.quit()

soup = BeautifulSoup(site, 'html.parser')
data = soup.find_all('tbody', attrs={'class': 'listtable responsive-table-data-mb'})

file = open('export_data.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['Job', 'Type', 'Application_Deadline', 'Salary']
writer.writerow(headers)

for title in data:
    Job = (title.find('data-th', attrs={
        'class': 'a'}).text)
    Type  = (title.find('data-th').text)
    Application_Deadline = (title.find('td', attrs={
        'class': 'mobile_hide'}).text)
    Salary = (title.find('data-th').text)
    
    new = open('export_data.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(new)
    headers = ([Job, Type, Application_Deadline, Salary])
    writer.writerow(headers)
    file.close()