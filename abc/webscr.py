import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

url = 'https://www.periodictable.one/elements/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find("table", {"class": "table table-hover table-sm table-sticky"})
rows = table.find_all("tr")

symbol_list = []
name_list = []
atomic_no_list = []


# Loop through the rows
for row in rows:
    data = row.find_all("td")
    if data:
        symbol = data[1].text.strip()
        symbol_list.append(symbol)
        name=data[2].text.strip()
        name_list.append(name)
        atomic_number = data[0].text.strip()
        atomic_no_list.append(atomic_number)

# Create a Pandas dataframe from the symbol list
df = pd.DataFrame({'Symbol': symbol_list,'name': name_list,'atomic': atomic_no_list})

# Show the dataframe
print(df)
st.write(df)
    


        # print(f"Element: {symbol} ({name}), Atomic Number: {atomic_number}")
        # st.write(f"Element: {symbol} ({name}), Atomic Number: {atomic_number} ")

