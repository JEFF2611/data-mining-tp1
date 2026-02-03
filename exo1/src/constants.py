c_URL = "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Le_saviez-vous_%3F/Archives/"
c_HEADERS = {"User-Agent": "Mozilla/5.0"}
c_CSV = "./data/quotes.csv"

#regex for date
date_regex =  r"((0[1-9]|[12][0-9]|3[01])\s(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s(\d{4}))"