from utils import get_quotes_from_year_to_year, write_quotes_to_csv
from constants import c_CSV

if __name__ == "__main__":
    quotes = get_quotes_from_year_to_year(2017, 2021)
    write_quotes_to_csv(quotes, c_CSV)
