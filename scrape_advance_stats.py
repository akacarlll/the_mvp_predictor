import requests
import random
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd
import os

url_start = "https://www.basketball-reference.com/leagues/NBA_{}_advanced.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


years = list(range(1980,2026))

def scrape_advanced_stats(years:list) :
    
    """_summary_
    """
    df_list = {}
    for year in tqdm(years):
        url = url_start.format(year)
        
        response = requests.get(url, headers=headers)
        wait_time = random.uniform(3, 5)
        time.sleep(wait_time)
        print(f"Waited for {wait_time:.2f} seconds before continuing.")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        stat_table = soup.find(id="advanced_stats")
        if stat_table is not None:
            stat = pd.read_html(str(stat_table))[0]
            df_list[year] = {'year': year, 'stat': stat}
        
        wait_time = random.uniform(0.5, 1.5)
        time.sleep(wait_time + 1)
        
    if not os.path.exists("advanced_stats_csv"):
        os.makedirs("advanced_stats_csv")

    for year, data in df_list.items():
        data['stat'].to_csv(f"advanced_stats_csv/advanced_stat{year}.csv", index=False)
        
scrape_advanced_stats(years)