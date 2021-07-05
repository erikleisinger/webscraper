from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import PyPDF2
import json

#Custom modules
from scraperFunctions import cleanup, extractData, getPdf
from constants import columnNames, dataFromFrontPage, PATH_TO_SCRAPER

# init scraper 

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": PATH_TO_SCRAPER + "downloads/pdf", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})

driver = webdriver.Chrome(options=options)

# BEGIN SCRAPE

# Landing page

driver.get("https://www.albertalobbyistregistry.ca/")

button = driver.find_elements_by_xpath("//a[.='Search Registry']")[0].click()

# Search page

search_button = driver.find_elements_by_xpath("//input[@name='Search']")[0].click()

# Switch to iFrame

iframe = driver.find_elements_by_xpath("//iframe")[0]
driver.switch_to.frame(iframe)

# Find table / row

table = driver.find_elements_by_xpath("//table[@id='15827219293901974']")[0]
table_rows = table.find_elements(By.TAG_NAME, "tr")

# Begin writing to output.js

f = open('output.js', "a")
f.write("[")

# Begin looping through rows
row = 1
while row < len(table_rows):
  
  this_row = table_rows[row]

  cols = this_row.find_elements(By.TAG_NAME, "td")

  values = {}
  for x in cols:
    header = x.get_attribute("headers")

    # Extract data from row cells that is not in pdf
    if (columnNames[header] in  dataFromFrontPage):
      values[columnNames[header]] = x.text
    
    #Download and extract data from pdf
    if columnNames[header] == 'View':
      try: 
        getPdf(driver, x)
        data = extractData()
        values = {**values, **data}
        f.write(json.dumps(values))
        f.write(',')
        cleanup()
      except Exception as e:
        errors = open('errorLog.txt', "a")
        errors.write('Row ' + str(row)  + ': ' + str(e))
        continue

  row+=1

#After looping through rows, complete the write to output.js and close the array of objects
f = open('output.js', "a")
f.write(']')

