import random
import time
import os


from _get_shot_charts import get_shot_chart
from best_scorer_ import get_top_players_by_season


def get_all_shot_charts(seasons, top_n=10):
    all_data = {}
    for season in seasons:
        print(f"Processing season: {season}")
        top_players = get_top_players_by_season(season, top_n)
        season_data = {}
        for _, player in top_players.iterrows():
            print(f"Fetching data for {player['PLAYER_NAME']} ({season})")
            try:
                shot_chart = get_shot_chart(player['PLAYER_ID'], season)
                season_data[player['PLAYER_NAME']] = shot_chart
                wait = random.uniform(0.0001,0.002)
                time.sleep(wait)
            except Exception as e:
                print(f"Error fetching data for {player['PLAYER_NAME']}: {e}")
        all_data[season] = season_data
    return all_data

current_season = "2023-24"
num_years = 10
start_year = int(current_season.split("-")[0]) - num_years + 1

seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(start_year, start_year + num_years)]

shot_charts = get_all_shot_charts(seasons)

output_dir = "nba_shot_charts"
os.makedirs(output_dir, exist_ok=True)

for season, players in shot_charts.items():
    season_dir = os.path.join(output_dir, season)
    os.makedirs(season_dir, exist_ok=True)
    for player, df in players.items():
        df.to_csv(os.path.join(season_dir, f"{season}_{player}_shot_chart.csv"), index=False)
