import sqlite3
import pandas
import re
import requests
from bs4 import BeautifulSoup

### YAHOO FINANCE SCRAPING
MOST_ACTIVE_STOCKS_URL = "https://cs1951a-s21-brown.github.io/resources/stocks_scraping_2021.html"

### STONKS API ###
STONKS_API_URL = "http://localhost:8000"

# TODO: Part 1: Use BeautifulSoup and requests to collect data required for the assignment.
r = requests.get("https://cs1951a-s21-brown.github.io/resources/stocks_scraping_2021.html", auth = ('user','pass'))

def scrape(soup, company_list, quotes_dict, company_names):
   
    for line in soup:

        company_name  = line.find("td", class_ = "left bold plusIconTd elp").text.strip()
        stock_symbol, HQ_state = line.find_all("td", class_ = None)[0].text.strip(), line.find_all("td", class_ = None)[1].text.strip().lower()
        company_names.append(stock_symbol)
        price = float(line.find("td", class_ = re.compile('^align')).text.strip().replace(',',''))
        change_percentage = float(line.find("td", class_ = re.compile('pcp$')).text.strip().replace('%',''))
        volume = float(line.find("td", class_ = re.compile('turnover')).text.strip().replace('M','0000').replace('K','0').replace('.',''))
        # print(company_name, stock_symbol, HQ_state, price, change_percentage, volume)
        company_list.append((stock_symbol, company_name, HQ_state))

        quotes_dict[stock_symbol] = (company_name, stock_symbol, HQ_state, price, change_percentage, volume)

def get_request(company_names, quotes_list, quotes_dict):
    req_l = []
    req1_l = []
    for i in company_names:
        req = requests.get(f'{STONKS_API_URL}/{i}/chart/1m').json()['charts']
        aaa = 0
        for j in range(len(req)):
            aaa += req[j]['close']
        aaa /= len(req)
        req_l.append(aaa)
        req1 = requests.get(f'{STONKS_API_URL}/{i}/chart/date/2023-01-20').json()['close']
        req1_l.append(req1)
        quotes_list.append((i,req1,quotes_dict[i][3],aaa,quotes_dict[i][5],quotes_dict[i][4]))



soup = BeautifulSoup(r.content, 'html.parser')
soup = soup.find('table', class_ = "genTbl closedTbl elpTbl elp25 crossRatesTbl")
soup = soup.find('tbody')
soup = soup.find_all('tr')
data = []
data1 = {}
data2 = []
company_names = []

scrape(soup, data, data1, company_names)
get_request(company_names,data2,data1)





# TODO: Save data below.

# TODO: Part 2: Use Stonks API to collect historical trading data for your stocks.
    
# print(req_l)
# print(req1_l)


# Create connection to database

#Make sure if are unable to connect make sure you have the right path to data.db, this might cause 
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "companies";')
c.execute('DROP TABLE IF EXISTS "quotes";')

# TODO: Part 4: Create tables in the database and add data to it. REMEMBER TO COMMIT
c.execute('CREATE TABLE companies (symbol text NOT NULL, name text NOT NULL, location text NOT NULL, PRIMARY KEY (symbol))')
conn.commit()
c.execute('CREATE TABLE quotes(symbol text NOT NULL, close float NOT NULL, price float NOT NULL, avg_price float NOT NULL, volume float NOT NULL, change_pct float NOT NULL, FOREIGN KEY(symbol) REFERENCES companies(symbol))')
conn.commit()
for t in data:

    c.execute('INSERT INTO companies (symbol,name,location) VALUES (?,?,?)', t)
    
conn.commit()

for l in data2:
    print(l[-2])
    c.execute('INSERT INTO quotes (symbol, close, price, avg_price, volume, change_pct) VALUES (?,?,?,?,?,?)', l)
    
conn.commit()