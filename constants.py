PATH_TO_SCRAPER = '/home/erik/scraper/'

columnNames = {
    "ITEM_002_DATE": "Date",
    "ITEM_003_CHAR": "Termination Date",
    "ITEM_005_CHAR": "Organization",
    "ITEM_006_CHAR": "Client Name",
    "ITEM_007_CHAR": "Designated Filer",
    "ITEM_008_CHAR": "Government Department Lobbied",
    "ITEM_009_CHAR": "Prescribed Provincial Entity Lobbied",
    "ITEM_010_CHAR": "Subject Matter of Lobbying",
    "ITEM_011_CHAR": "Registration Number",
    "ITEM_012_CHAR": "Type of Lobbyist",
    "ITEM_013_CHAR": "Lobbyists",
    "ITEM_014_CHAR": "Type of Registration",
    "ITEM_015_CHAR": "Registration Status",
    "ITEM_016_CHAR": "View",
  }

dataFromFrontPage = [
    "Date",
    "Designated Filer",
    "Subject Matter of Lobbying",
    "Type of Lobbyist",
    "Registration Status",
  ]

regex = {
  "businessInformation": "Business Address:\n(.*?)(?:Consultant(.*))?\s*Lobbyist",
  "designatedFilerInformation": "Designated Filer Information\n(.*?)Business Address",
  "registrationInformation": "Registration Information\n(.*?)Designated Filer"
  }
  

  