import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
import random

def scrape_nba_salaries(year, base_path):
    """
    Scrape les données de salaires NBA pour une année donnée et les enregistre dans un fichier CSV.
    Arguments :
        year (int) : Année des données de salaires.
        base_path (str) : Chemin de sauvegarde des fichiers CSV.
    """
    base_url = f'https://www.espn.com/nba/salaries/_/year/{year}/page/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    data = {
        'RK': [],
        'NAME': [],
        'TEAM': [],
        'SALARY': []
    }

    page = 1
    while True:
        print(f"Scraping year {year}, page {page}...")
        url = base_url + str(page)
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            salary_table = soup.find('table', class_='tablehead')
            if not salary_table:
                print(f"No table found for year {year}, page {page}. Ending year scraping.")
                break

            rows = salary_table.find_all('tr')[1:]  # Skip header row
            if not rows:
                print(f"No data found for year {year}, page {page}. Ending year scraping.")
                break

            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 4:
                    data['RK'].append(cols[0].text.strip())
                    data['NAME'].append(cols[1].text.strip())
                    data['TEAM'].append(cols[2].text.strip())
                    salary = cols[3].text.strip().replace('$', '').replace(',', '')
                    data['SALARY'].append(salary)

            page += 1
            x = random.uniform(0.1, 2)
            time.sleep(x)  # Random delay to be polite
            print(f"Sleep for {x} seconds")
        except requests.exceptions.RequestException as e:
            print(f"HTTP request error for year {year}, page {page}: {e}")
            break
        except Exception as e:
            print(f"Error for year {year}, page {page}: {e}")
            break

    df = pd.DataFrame(data)
    if not df.empty:
        file_path = os.path.join(base_path, f'nba_salaries_{year}.csv')
        df.to_csv(file_path, index=False)
        print(f"Data for year {year} saved to {file_path}")
    else:
        print(f"No data scraped for year {year}.")


def main():
    base_path = r'C:\Users\carlf\Documents\GitHub\The_Great_MVP_Predictor\data\players_salaries'
    os.makedirs(base_path, exist_ok=True)  # Crée le répertoire si nécessaire

    start_year = 2010
    end_year = 2025

    for year in range(start_year, end_year + 1):
        scrape_nba_salaries(year, base_path)
        

if __name__ == "__main__":
    main()
