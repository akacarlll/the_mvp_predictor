from nba_api.stats.endpoints import leaguedashplayerstats

def get_top_players_by_season(season, top_n=10):
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        season_type_all_star='Regular Season'
    )
    df = stats.get_data_frames()[0]
    top_players = df.nlargest(top_n, 'PTS')[['PLAYER_ID', 'PLAYER_NAME', 'PTS']]
    return top_players