import requests as re
from bs4 import BeautifulSoup as bs

URL = 'https://www.forbes.com/digital-assets/crypto-prices/?sh=61beb4582478'
NUM_OF_ROWS = 12
NUM_OF_COLS = 8

def get_cyrpto_data():
    html_table = get_html_from_crypto_page()
    if html_table != 500:
        headers = parse_header_data(html_table)
        crypto_rows = parse_crypto_row_data(html_table)
        return headers, crypto_rows
    else:
        return None

def get_html_from_crypto_page():
    try:
        response = re.get(URL)
        if response.status_code == 200:
            html_ = response.text
            soup = bs(html_, 'html.parser')
            html_table = soup.find('table', class_ = 'Table_tableContainer__Dm0uG')
            return html_table
    except Exception as e:
        if type(e) == re.exceptions.ConnectionError:
            return 500

def parse_header_data(html_table):
    thead_html = html_table.find('thead')
    header_row = thead_html.find('tr')
    headers = [header.text.strip() for header in header_row.find_all('th')[:NUM_OF_COLS]]
    return headers

def parse_crypto_row_data(html_table):
    crypto_rows = []
    tbody_html = html_table.find('tbody')
    tbody_html_rows = tbody_html.find_all('tr')[:NUM_OF_ROWS]

    for row in tbody_html_rows:
        temp_row = [td.text.strip() for td in row.find_all('td')[:NUM_OF_COLS]]
        crypto_rows.append(temp_row)
    return crypto_rows