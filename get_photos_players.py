import requests
import csv
from nba_api.stats.static import players
import time
import random
from tqdm import tqdm

# Fetch NBA player metadata
nba_players = players.get_players()

# Prepare CSV data
player_data = []
base_image_url = "https://cdn.nba.com/headshots/nba/latest/1040x760/{player_id}.png"
x = 0
for player in nba_players:
    player_id = player['id']
    image_url = base_image_url.format(player_id=player_id)
    
    # Check if the image URL is valid
    response = requests.head(image_url)
    if response.status_code == 200:
        player_data.append({
            "Player Name": player['full_name'],
            "Player ID": player_id,
            "Image URL": image_url
        })
        print(f"Player found: {player['full_name']} (ID: {player_id})")
    x += 1
    if x %100 == 0 :
        time.sleep(random.uniform(0.5, 1.5))
        print("waiting")
        
# Save to CSV
csv_file = "nba_players_faces.csv"
csv_columns = ["Player Name", "Player ID", "Image URL"]

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(player_data)
    print(f"CSV file '{csv_file}' created successfully!")
except Exception as e:
    print(f"Error while creating CSV: {e}")