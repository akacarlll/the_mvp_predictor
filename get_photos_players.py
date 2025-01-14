import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
base_url = "https://www.basketball-reference.com/players/"

# Function to get player images
def get_player_images():
    images = []
    for letter in "abcdefghijklmnopqrstuvwxyz":  # Iterate through player index pages
        url = f"{base_url}{letter}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        for row in soup.select("tr.full_table"):  # Select player rows
            name = row.find("th").get_text()
            link = row.find("a")["href"]
            player_page = f"https://www.basketball-reference.com{link}"
            
            # Scrape player page for image
            player_response = requests.get(player_page)
            player_soup = BeautifulSoup(player_response.content, "html.parser")
            img_tag = player_soup.find("img", {"class": "player-headshot"})
            if img_tag:
                images.append({"name": name, "image_url": img_tag["src"]})
    return pd.DataFrame(images)

# Save the data
df = get_player_images()
df.to_csv("nba_player_images.csv", index=False)
