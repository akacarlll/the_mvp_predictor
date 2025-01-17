
import requests
import csv
import pandas
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

# Fetch NBA player metadata
nba_players = players.get_players()

# Divide the list into three parts
total_players = len(nba_players)
chunk_size = total_players // 3
nba_players_parts = [
    nba_players[:chunk_size],  # First part
    nba_players[chunk_size:2 * chunk_size],  # Second part
    nba_players[2 * chunk_size:]  # Third part
]


# Base URL for player images
base_image_url = "https://cdn.nba.com/headshots/nba/latest/1040x760/{player_id}.png"

# Function to scrape player data for a given chunk
def scrape_player_data(player_chunk, output_file):
    player_data = []
    for player in player_chunk:
        player_id = player['id']
        image_url = base_image_url.format(player_id=player_id)
        # Fetch additional temporal information
        try:
            player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_dict()
            player_stats = player_info['resultSets'][0]['rowSet'][0]
            
            # Extract temporal information
            from_year = player_stats[22]  # FROM_YEAR
            to_year = player_stats[23]    # TO_YEAR
            draft_year = player_stats[27]  # DRAFT_YEAR
        except Exception as e:
            from_year = None
            to_year = None
            draft_year = None
            print(f"Error fetching data for player {player['full_name']}: {e}")
        
        # Check if the image URL is valid
        response = requests.head(image_url)
        if response.status_code == 200:
            player_data.append({
                "Player Name": player['full_name'],
                "Player ID": player_id,
                "Image URL": image_url,
                "From Year": from_year,
                "To Year": to_year,
                "Draft Year": draft_year,
            })
    
    # Save the chunk data to a CSV
    csv_columns = ["Player Name", "Player ID", "Image URL", "From Year", "To Year", "Draft Year"]
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(player_data)
        print(f"CSV file '{output_file}' created successfully!")
    except Exception as e:
        print(f"Error while creating CSV: {e}")

# Scrape data for each part and save to separate CSV files
# scrape_player_data(nba_players_parts[0], "nba_players_part1.csv")
# scrape_player_data(nba_players_parts[1], "nba_players_part2.csv")
scrape_player_data(nba_players_parts[2], "nba_players_part3.csv")
