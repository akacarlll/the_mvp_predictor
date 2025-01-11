from nba_api.stats.endpoints import leaguegamefinder
import requests
import pandas as pd

def get_games_by_season(season):
    gamefinder = leaguegamefinder.LeagueGameFinder(
        season_nullable=season,
        season_type_nullable='Regular Season'
    )
    games = gamefinder.get_data_frames()[0]
    
    nba_teams = [
        "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets",
        "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets",
        "Detroit Pistons", "Golden State Warriors", "Houston Rockets",
        "Indiana Pacers", "LA Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
        "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans",
        "New York Knicks", "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers",
        "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs",
        "Toronto Raptors", "Utah Jazz", "Washington Wizards"
    ]
    
    games = games[games['TEAM_NAME'].isin(nba_teams)]
    
    return games