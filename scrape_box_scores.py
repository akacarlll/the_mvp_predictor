from get_box_scores import get_boxscore, get_games_by_season
import os


def get_all_boxscores(seasons):
    all_boxscores = {}
    for season in seasons:
        print(f"Processing season: {season}")
        games = get_games_by_season(season)
        season_boxscores = []

        for count, game_id in enumerate(games['GAME_ID'], start=1):
            #print(f"Fetching boxscore for GAME_ID: {game_id}")
            try:
                player_stats, team_stats = get_boxscore(game_id)
                season_boxscores.append({
                    'GAME_ID': game_id,
                    'player_stats': player_stats,
                    'team_stats': team_stats
                })
            except Exception as e:
                print(f"Error fetching boxscore for GAME_ID {game_id}: {e}")
                
            if count % 50 == 0:
                print(f"{count} boxscore have been fetched.") 
        
        all_boxscores[season] = season_boxscores
    return all_boxscores

seasons = ["2020-21"]
    #"2015-16", "2016-17", "2017-18", 
    #        "2018-19", "2019-20", "2020-21", "2021-22"]
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
