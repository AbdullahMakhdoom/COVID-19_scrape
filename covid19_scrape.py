#importing modules
import requests
from bs4 import BeautifulSoup

# URL address for scraping COVID-19 data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []

# soup.find_all('td') will scrape every element in the url's table
data_iterator = iter(soup.find_all('td'))
#data_iterator is the iterator of the table


# convert while loop to for loop using simple soup.find_all('td')
########################################################
# Loop until data is available in iterator
while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text


        # For 'confirmed' and 'deaths', remove the commas and convert to int
        data.append((
            country,
            int(confirmed.replace(',', '')),
            int(deaths.replace(',', '')),
            continent
        ))

    except StopIteration:
        break

#Sor the data by the number of confirmed cases
data.sort(key = lambda row:row[1], reverse = True)

# For printing data in human readable format, using 'texttable'
# create texttable object
table = tt.Texttable()
# add an empty row at the beginning for the headers
table.add_rows([(None, None, None, None)] + data)
# 'l' denotes left, 'c' denotes center, and 'r' denotes right
table.set_cols_align(('c','c','c','c'))
table.headers(('Country', 'Number of cases', 'Deaths', 'Continent'))

print(table.draw())
