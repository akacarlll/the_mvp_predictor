from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

def get_games_by_season(season):
    gamefinder = leaguegamefinder.LeagueGameFinder(
        season_nullable=season,
        season_type_nullable='Regular Season'
    )
    games = gamefinder.get_data_frames()[0]
    return games