from nba_api.stats.endpoints import boxscoretraditionalv2

def get_boxscore(game_id):
    boxscore = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id)
    player_stats = boxscore.player_stats.get_data_frame()  # Statistiques des joueurs
    team_stats = boxscore.team_stats.get_data_frame()      # Statistiques des équipes
    return player_stats, team_stats
