import PyPDF2
import re
from constants import regex
from getValues import getValues

def getRegistrationInformation(text):
  allInfo = re.findall(regex['registrationInformation'], text, flags = re.DOTALL)[0].strip().split('\n')

  return getValues(allInfo)

def getDesignatedFilerInformation(text):
  allInfo = re.findall(regex['designatedFilerInformation'], text, flags = re.DOTALL)[0].strip().split('\n')

  businessInfoArray = re.findall(regex['businessInformation'], text, flags = re.DOTALL)[0][0].strip().split('\n')


  businessAddress = None
  designatedFilerInfo = None

  try: 
    businessAddress = getValues(businessInfoArray)

  except:
    return None

  try:
     designatedFilerInfo = getValues(allInfo)

  except: 
    return None

  designatedFilerInfo['Business Address'] = businessAddress

  return designatedFilerInfo