"""
projekt_3v2.py: treti projekt Engeto akademie
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
    ["code", "location", "registered", "envelopes","valid",]
]
def getCommandLineArguments():
    arguments = sys.argv[1:]
    if arguments[1].split(".")[1] == "csv":
        return arguments
    else:
        arguments[1] += ".csv" 
        return arguments

def addAllAvailableParties(url = "ps311?xjazyk=CZ&xkraj=2&xobec=530158&xvyber=2101"):
    data = getDataFromCity(url, False)
    data = data[27:]
    data = data[:65] + data[72:]

    parties = []

    for i in range(len(data)):
        if i % 5 == 0:
            parties.append(data[i])
    dataToCSV[0].extend(parties)


def getSoupFromURL(url = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    return soup

def getLinksForCities(soup):
    listOfLinks = []
    for link in soup.find_all('a'):
        if re.match(r'^\d+(\.\d+)?$', link.get_text()):
            listOfLinks.append(link.get('href'))
    return listOfLinks

def getDataFromCity(linkToCity, justSoup = True):
    citySoup = getSoupFromURL("https://volby.cz/pls/ps2017nss/" + linkToCity)
    if justSoup:
        return citySoup
    else:
        tables = citySoup.find_all('table')
        cityData = []

        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all(['th', 'td'])
                for cell in cells:
                    cityData.append(cell.get_text())
        return cityData

def getDataFromAllCities(citiesLinks):
    citiesData = [
    ]
    for i in range(len(citiesLinks)):
        citySoup = getDataFromCity(citiesLinks[i])
        cityTables = getDataFromCity(citiesLinks[i], False)

        code = re.search("&xobec=(\d+)",citiesLinks[i]).group(1)
        location = re.search("Obec:\s*(\S+)", str(citySoup.find_all('h3')[2])).group(1)
        registered = cityTables[13]
        envelopes = cityTables[14]
        valid = cityTables[16]

        citiesData.append([code, location, registered, envelopes, valid] + getVotesForAllParties(cityTables))
    return citiesData

def getVotesForAllParties(table):
    data = table
    data = data[27:]
    data = data[:65] + data[72:]

    parties = []

    for i in range(len(data)):
        if i % 5 == 0:
            parties.append(data[i + 1])
    return parties

def writeToCSVFile(data, fileName):

    with open(fileName, mode='w') as csvFile:
        csvWriter = csv.writer(csvFile)

        for row in data:
            csvWriter.writerow(row)

def run():
    
    try:
        arguments = getCommandLineArguments()
        soup = getSoupFromURL(arguments[0])
        print(f'Web scraping the url:\n{arguments[0]}')
        citiesLinks = getLinksForCities(soup)

        addAllAvailableParties()

        dataToCSV.extend(getDataFromAllCities(citiesLinks))
        print(f'Saving the data in {arguments[1]}')
        writeToCSVFile(dataToCSV, arguments[1])
    except(IndexError):
        print("Please add arguments! example: python projekt3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102' 'example.csv'")
    except Exception as e:
        print(str(e))
run()
