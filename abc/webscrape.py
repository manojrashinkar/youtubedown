    import requests
    from bs4 import BeautifulSoup
    import streamlit as st
    import pandas as pd

    url = 'https://www.periodictable.one/elements/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find("table", {"class": "table table-hover table-sm table-sticky"})
    rows = table.find_all("tr")

    for row in rows:
        data = row.find_all("td")
        if data:
            symbol = data[1].text.strip()
            name = data[2].text.strip()
            atomic_number = data[0].text.strip()
            atomic_number1 = data[3].text.strip()
            print(type(name))
        


            # print(f"Element: {symbol} ({name}), Atomic Number: {atomic_number}")
            # st.write(f"Element: {symbol} ({name}), Atomic Number: {atomic_number} ")

