"""
projekt_3.py: treti projekt Engeto akademie
author: Patrik Bocek
email: patrik.bocek@tria-tr.cz
discord: Patrik B fallencz#2217
"""

import csv
from bs4 import BeautifulSoup
import requests
import re
import sys

dataToCSV = [
    ["code", "location", "registered", "envelopes", "valid"],
]

def getCommandLineArguments():
    arguments = sys.argv[1:]
    if len(arguments) != 2:
        raise ValueError("Please provide both the URL and the output file name as command line arguments.")
    if not arguments[0].startswith("https://volby.cz"):
        raise ValueError("Invalid URL provided. Please use a valid URL from https://volby.cz.")
    return arguments

# ... (zbytek kódu zůstává nezměněný)

def run():
    try:
        arguments = getCommandLineArguments()
        url, output_file = arguments
        soup = getSoupFromURL(url)
        print(f'Web scraping the URL:\n{url}')
        cities_links = getLinksForCities(soup)

        addAllAvailableParties()

        dataToCSV.extend(getDataFromAllCities(cities_links))
        print(f'Saving the data in {output_file}')
        writeToCSVFile(dataToCSV, output_file)
    except ValueError as ve:
        print(str(ve))
    except Exception as e:
        print(str(e))

run()
