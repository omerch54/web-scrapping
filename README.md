# Web Scraping for Stock Market Data

## Overview
This project scrapes stock market data from Yahoo Finance and uses an API (STONKS API) to retrieve historical trading data. The collected data is stored in an SQLite database for further analysis.

## Features
- **Web Scraping**: Uses `BeautifulSoup` and `requests` to extract stock data from a web page.
- **API Integration**: Fetches historical stock prices from an external API.
- **Database Storage**: Stores extracted data in an SQLite database.
- **SQL Queries**: Provides predefined SQL queries to retrieve and analyze stock information.

## File Structure
- `main_a.py`: Main script for web scraping and database management.
- `data.db`: SQLite database storing stock market data.
- `query1.sql`, `query2.sql`, `query3.sql`, `query4.sql`: SQL queries for data retrieval.

## Requirements
- Python 3.x
- SQLite3
- BeautifulSoup
- Requests
- Pandas
- Regular Expressions (`re`)

## Installation
1. Clone this repository:
   ```sh
   git clone <repository-url>
   cd <repository>
   ```
2. Install dependencies:
   ```sh
   pip install requests beautifulsoup4 pandas
   ```

## Usage
### Running the Scraper
To scrape data and populate the database, run:
```sh
python main_a.py
```

### Querying Data
Run SQL queries using:
```sh
sqlite3 data.db
```
Execute queries:
```sql
SELECT * FROM companies;
SELECT * FROM quotes;
```

## Data Schema
### `companies` Table
| Column  | Type   | Description                |
|---------|--------|----------------------------|
| symbol  | TEXT   | Stock symbol (Primary Key) |
| name    | TEXT   | Company name               |
| location | TEXT  | Company headquarters       |

### `quotes` Table
| Column       | Type  | Description                    |
|-------------|--------|--------------------------------|
| symbol      | TEXT   | Stock symbol (Foreign Key)    |
| close       | FLOAT  | Closing price                 |
| price       | FLOAT  | Latest stock price            |
| avg_price   | FLOAT  | Average stock price (1 month) |
| volume      | FLOAT  | Trading volume                |
| change_pct  | FLOAT  | Percentage change in price    |

## Contributors
- **Omer** & BrownU DSI

## License
This project is licensed under the Brown Uni License.
