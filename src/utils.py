#libraries imports
import requests, dateparser, re
from bs4 import BeautifulSoup
import pandas as pd
from constants import c_URL, c_HEADERS, date_regex


def get_data(url : str):
    """Get the data from the url"""
    response = requests.get(url, headers=c_HEADERS)
    return response

def get_quotes(url : str) -> pd.DataFrame:
    """Get the quotes from the url"""
    response = get_data(url)
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    body = soup.find('div', {'class': 'mw-content-ltr'})
    
    ul = body.find('ul')
    quotes = []
    #We loop through the children of the ul element, to not get too deep in the html tree
    for quote in ul.children:
        if quote.name == 'li':
            #We get the date of the quote
            dl_content = quote.find('dl').text.strip("\n")
            #We parse the date
            date_to_parse = re.search(date_regex, dl_content).group()
            date = dateparser.parse(date_to_parse, date_formats=["%d %B %Y"])
            #We add the quote to the dataframe
            quotes.append({"year": date.year, "month": str(date.strftime("%B")) , "quote": quote.text.strip("\n")})
    return pd.DataFrame(quotes)

def get_quotes_from_year_to_year(year_start : int, year_end : int) -> pd.DataFrame:
    """Get the quotes from the year_start to year_end"""
    quotes_df = pd.DataFrame()
    for year in range(year_start, year_end + 1):
        quotes_df = pd.concat([quotes_df, get_quotes(c_URL + str(year))])
    return quotes_df

def write_quotes_to_csv(quotes_df : pd.DataFrame, file_path : str):
    """Write the quotes to a csv file"""
    quotes_df.to_csv(file_path, index=False)