from _get_box_scores import get_boxscore
from get_games_name import get_games_by_season
import os


def get_all_boxscores(seasons):
    all_boxscores = {}
    for season in seasons:
        print(f"Processing season: {season}")
        games = get_games_by_season(season)
        season_boxscores = []
        
        for game_id in games['GAME_ID']:
            print(f"Fetching boxscore for GAME_ID: {game_id}")
            try:
                player_stats, team_stats = get_boxscore(game_id)
                season_boxscores.append({
                    'GAME_ID': game_id,
                    'player_stats': player_stats,
                    'team_stats': team_stats
                })
            except Exception as e:
                print(f"Error fetching boxscore for GAME_ID {game_id}: {e}")
        
        all_boxscores[season] = season_boxscores
    return all_boxscores

# Exemple pour les 10 dernières saisons
seasons = ["2023-2024"]
    # "2013-14", "2014-15", "2015-16", "2016-17", "2017-18", 
    #        "2018-19", "2019-20", "2020-21", "2021-22", "2022-23"]
boxscores = get_all_boxscores(seasons)

output_dir = "nba_boxscores"
os.makedirs(output_dir, exist_ok=True)

for season, games in boxscores.items():
    season_dir = os.path.join(output_dir, season)
    os.makedirs(season_dir, exist_ok=True)
    for game in games:
        player_stats_file = os.path.join(season_dir, f"{game['GAME_ID']}_player_stats.csv")
        team_stats_file = os.path.join(season_dir, f"{game['GAME_ID']}_team_stats.csv")
        
        game['player_stats'].to_csv(player_stats_file, index=False)
        game['team_stats'].to_csv(team_stats_file, index=False)
