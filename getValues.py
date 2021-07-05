def getValues(array):
  x = 0
  obj = {}
  while x < len(array):
    try: 
      obj[array[x]] = array[x+1]
      x += 2
    except Exception: 
      logger.error('There was an error processing this object: ', obj)

  return obj