Engeto Project 3 version 2
# Web Scraper for 2017 Czech Republic Parliament Votes
**This web scrapper uses beautiful soup to scrape the Czech Republics Parliament votes on the czech statistics institute website based on the region**

### To use this web scrapper you need to install the needed libraries 
To install the required libraries run:
```
pip install -r requirements.txt
```

### To run the web scraper run
 - The first argument needs to be a url address from this website: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ
 - The second argument is the file name you want to use for the csv result table.
```
python3 project.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "example.csv"
```

## Example
```
python3  projekt3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" "example.csv"
Web scraping the url:
https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102
Saving the data in example.csv
```
