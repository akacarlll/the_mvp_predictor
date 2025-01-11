import requests
import random
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os

url_start = "https://www.basketball-reference.com/contracts/players.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def scrape_2024_salaries(headers):
    """Scrapes NBA player salary data from Basketball Reference."""
    url = "https://www.basketball-reference.com/contracts/players.html"
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return

    wait_time = random.uniform(3, 5)
    time.sleep(wait_time)
    print(f"Waited for {wait_time:.2f} seconds before parsing the page.")

    soup = BeautifulSoup(response.content, 'html.parser')

    stat_table = soup.find("table", id="player-contracts")
    if stat_table is None:
        print("Error: Could not find the table with ID 'player-contracts'")
        return
    
    # Extract table headers
    headers = [th.getText() for th in stat_table.find_all('th')][1:]  # Skip the first empty header

    # Extract table rows
    rows = stat_table.find_all('tr')
    data = []
    for row in rows:
        cells = row.find_all('td')
        if cells:
            data.append([cell.getText().strip() for cell in cells])
    output_dir = "players_salaries"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "NBA_players_salaries.csv")
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data) 

    print(f"Data successfully saved to {output_file}")

scrape_2024_salaries(headers=headers)