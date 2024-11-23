from nba_api.stats.endpoints import shotchartdetail

# Exemple pour la saison 2022-23
def get_shot_chart(player_id, season):
    response = shotchartdetail.ShotChartDetail(
        team_id=0,  # Aucun filtre pour l'équipe
        player_id=player_id,
        season_nullable=season,
        season_type_all_star='Regular Season'
    )
    shot_data = response.get_data_frames()[0]
    return shot_data

