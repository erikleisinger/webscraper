from selenium.webdriver.common.by import By
import os
import PyPDF2
import time

#Custom modules
from getters import getRegistrationInformation, getDesignatedFilerInformation
from constants import PATH_TO_SCRAPER

def checkDownload():
  while any(os.listdir(PATH_TO_SCRAPER + "downloads/pdf")) == False:
    time.sleep(2)
    print('File not yet downloaded. Waiting for download...')
  
  print('File downloaded. Continuing...')
  return


def getPdf(driver, element):
  try: 
    href = element.find_elements(By.TAG_NAME, "a")[0].click()
    checkDownload()
    return
  except Exception as e:
    raise e
  
  
    
def getPdfText():
  pdf = ""
  try:
    pdf = open(PATH_TO_SCRAPER + 'downloads/pdf/registration_form_for_organization_lobbyists.pdf', 'rb')
  except: 
    pass

  try: 
    pdf = open(PATH_TO_SCRAPER + 'downloads/pdf/registration_form_for_consultant_lobbyists.pdf', 'rb')
  except:
    pass

  pdf_read = PyPDF2.PdfFileReader(pdf)

  numPages = pdf_read.numPages

  i = 0
  pdf_text = ""

 
  while i < numPages:
    page_text = pdf_read.getPage(i).extractText()
    pdf_text += page_text
    i += 1

  return pdf_text

def extractData():
  text = getPdfText()

  info = {}

  info['Registration Information'] = getRegistrationInformation(text)
  info['Designated Filer Information'] = getDesignatedFilerInformation(text)

  return info


def cleanup():
  try:
    file = 'registration_form_for_organization_lobbyists.pdf'
    location = PATH_TO_SCRAPER + 'downloads/pdf'
    path = os.path.join(location, file)
    os.remove(path)
  except: 
    pass

  try: 
    file = 'registration_form_for_consultant_lobbyists.pdf'
    location = PATH_TO_SCRAPER + 'downloads/pdf'
    path = os.path.join(location, file)
    os.remove(path)
  except:
    pass
  