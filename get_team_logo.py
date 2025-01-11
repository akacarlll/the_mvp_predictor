import pandas as pd
import os 
# Creating the dataset
data = {
    "Equipe": [
        "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", 
        "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", 
        "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers", 
        "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", 
        "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks", 
        "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", 
        "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", 
        "Utah Jazz", "Washington Wizards"
    ],
    "TEAM_ABBREVIATION" :[
    "ATL", "BOS", "BKN", "CHA", "CHI", "CLE", "DAL", "DEN", 
    "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", 
    "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHX", 
    "POR", "SAC", "SAS", "TOR", "UTA", "WAS"
    ],
    "Logo": [
        "https://upload.wikimedia.org/wikipedia/en/2/24/Atlanta_Hawks_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/8/8f/Boston_Celtics.svg",
        "https://upload.wikimedia.org/wikipedia/en/4/44/Brooklyn_Nets_newlogo.svg",
        "https://upload.wikimedia.org/wikipedia/en/c/c4/Charlotte_Hornets_%282014%29.svg",
        "https://upload.wikimedia.org/wikipedia/en/6/67/Chicago_Bulls_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/4/4b/Cleveland_Cavaliers_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/9/97/Dallas_Mavericks_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/7/76/Denver_Nuggets.svg",
        "https://upload.wikimedia.org/wikipedia/en/1/1e/Detroit_Pistons_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/0/01/Golden_State_Warriors_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/2/28/Houston_Rockets.svg",
        "https://upload.wikimedia.org/wikipedia/en/1/1b/Indiana_Pacers.svg",
        "https://upload.wikimedia.org/wikipedia/en/b/bb/Los_Angeles_Clippers_logo.svg",
        "https://upload.wikimedia.org/wikipedia/commons/3/3c/Los_Angeles_Lakers_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/f/f1/Memphis_Grizzlies.svg",
        "https://upload.wikimedia.org/wikipedia/en/f/fb/Miami_Heat_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/4/4a/Milwaukee_Bucks_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/c/c2/Minnesota_Timberwolves_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/0/0d/New_Orleans_Pelicans_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/2/25/New_York_Knicks_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/5/5d/Oklahoma_City_Thunder.svg",
        "https://upload.wikimedia.org/wikipedia/en/1/10/Orlando_Magic_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/0/0e/Philadelphia_76ers_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/d/dc/Phoenix_Suns_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/2/21/Portland_Trail_Blazers_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/c/c7/SacramentoKings.svg",
        "https://upload.wikimedia.org/wikipedia/en/a/a2/San_Antonio_Spurs.svg",
        "https://upload.wikimedia.org/wikipedia/en/3/36/Toronto_Raptors_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/c/c9/Utah_Jazz_logo.svg",
        "https://upload.wikimedia.org/wikipedia/en/0/02/Washington_Wizards_logo.svg"
    
    ]
}

# Creating the DataFrame
df = pd.DataFrame(data)

output_dir = "nba_logos"
os.makedirs(output_dir, exist_ok=True)
# Saving the DataFrame to a CSV file

file_path = os.path.join(output_dir, "nba_team_logos.csv")
df.to_csv(file_path, index=False)
