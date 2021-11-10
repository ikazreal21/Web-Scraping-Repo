import requests
from bs4 import BeautifulSoup
import pandas as pd

web_url = requests.get(
    'https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area'
).text

soup = BeautifulSoup(web_url, 'lxml')

my_table = soup.find('table', {'class': 'wikitable sortable'})
# print(my_table)

df = pd.read_html(str(my_table))

df = df.to_frame()

print(df)
