# src/final/scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_launch_sites(url):
    """
    Scrape launch site data from a given Wikipedia page.
    """
    expected_columns = [
        "Country",
        "Location",
        "Coordinates",
        "Operational date",
        "Number of rocket launches",
        "Heaviest rocket launched",
        "Highest achieved altitude",
        "Notes"
    ]

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    all_tables = soup.find_all("table", class_="wikitable")

    df_list = []
    for table in all_tables:
        header_row = table.find("tr")
        if not header_row:
            continue
        headers = [th.get_text(strip=True) for th in header_row.find_all("th")]
        
        if "Country" in headers and "Coordinates" in headers:
            rows = table.find_all("tr")[1:]
            table_data = []
            for tr in rows:
                tds = tr.find_all(["td", "th"])
                row_data = [td.get_text(strip=True) for td in tds]
                if len(row_data) >= len(expected_columns):
                    row_data = row_data[:len(expected_columns)]
                    table_data.append(row_data)
            
            if table_data:
                region_df = pd.DataFrame(table_data, columns=expected_columns)
                df_list.append(region_df)

    if not df_list:
        raise Exception("No suitable launch site tables found.")
    return pd.concat(df_list, ignore_index=True)
