# Web Scraper - Alberta Lobbyist Registry

## Description

The result of a Saturday afternoon learning how webscrapers work (also Python).
This webscraper should collect a small bit of data from the first 10 or so rows of the Alberta Lobbyist Registry. 


## Dependencie
- Python 3
- Selenium (v. 3.14)
- PyPDF2 (latest)

## To Run *

- Go into constants.py and change the value of PATH_TO_SCRAPER to the absolute path of the scraper directory.
- Run `source bin/activate` to run the python3 venv
- In the root project folder, run `python3 scraper.py`

* I believe this is all you have to do to get this to run; I don't have much (any) experience publishing python programs so I might be missing something. 

## Output
- Any errors should be logged in errorLog.txt
- The scraper should take (some) data from the first 10 or so rows (including pdf) and write it to output.js
> - Output is in JSON format (I'm in JavaScript web-developer mode) but it could really be any format with some tweaks

## Known bugs (to fix)
- There is an issue after row 12 where Selenium is unable to click the next row; I believe the 'back-to-top' arrow is interfering.. Will require debugging and further learning about how selenium works

## Still to do 
- Better error logging
- Scraping all data from the pdfs
- Looping through all 800+ pages of the Registry

