from nba_api.stats.endpoints import leaguestandings
from nba_api.stats.static import teams
import pandas as pd
import time
from datetime import datetime
import os

def get_season_year(year):
    """
    Convertit une année en format de saison NBA (ex: 2023 -> '2022-23')
    """
    return f"{year-1}-{str(year)[2:]}"

def get_standings(season):
    """
    Récupère le classement NBA pour une saison donnée via l'API NBA.
    
    Args:
        season (str): La saison au format 'YYYY-YY' (ex: '2022-23')
    
    Returns:
        pandas.DataFrame: Le classement des équipes
    """
    try:
        # Récupération des données via l'API NBA
        standings = leaguestandings.LeagueStandings(
            season=season,
            season_type='Regular Season'
        )
        
        # Conversion en DataFrame
        df = standings.get_data_frames()[0]
        
        # Sélection et renommage des colonnes pertinentes
        columns_mapping = {
            'TeamCity': 'City',
            'TeamName': 'Team',
            'Conference': 'Conference',
            'ConferenceRecord': 'ConferenceRecord',
            'PlayoffRank': 'Rank',
            'WINS': 'W',
            'LOSSES': 'L',
            'WinPCT': 'Win%',
            'HOME': 'Home',
            'ROAD': 'Road',
            'L10': 'Last10',
        }
        
        df = df[columns_mapping.keys()].rename(columns=columns_mapping)
        
        # Ajout de la saison
        df['Season'] = season
        
        # Ajout de la colonne Year (deuxième année de la saison)
        df['Year'] = int(f"19{season.split('-')[1]}")
        
        # Création d'une colonne avec le nom complet de l'équipe
        df['FullTeamName'] = df['City'] + ' ' + df['Team']
        
        return df
        
    except Exception as e:
        print(f"Erreur lors de la récupération des données pour la saison {season}: {str(e)}")
        return None

def get_and_save_standings(start_year, end_year, output_dir="nba_standings"):
    """
    Récupère et sauvegarde les classements NBA pour chaque saison dans des fichiers séparés.
    
    Args:
        start_year (int): Année de début
        end_year (int): Année de fin
        output_dir (str): Dossier de sortie pour les fichiers CSV
    """
    # Création du dossier de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)
    
    for year in range(start_year, end_year + 1):
        season = get_season_year(year)
        print(f"Récupération des données pour la saison {season}")
        
        standings = get_standings(season)
        if standings is not None:
            # Création du nom de fichier
            filename = os.path.join(output_dir, f"nba_standings_{standings['Year'].iloc[0]}.csv")
            
            # Sauvegarde dans un fichier CSV
            standings.to_csv(filename, index=False)
            print(f"Données sauvegardées dans {filename}")
            
        # Petite pause entre les requêtes
        time.sleep(1)

def analyze_standings_by_year(output_dir="nba_standings"):
    """
    Analyse les classements pour chaque année.
    
    Args:
        output_dir (str): Dossier contenant les fichiers CSV
    """
    all_files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
    
    for file in all_files:
        year = file.split('_')[-1].split('.')[0]
        df = pd.read_csv(os.path.join(output_dir, file))
        
        print(f"\nAnalyse pour l'année {year}:")
        print("Top 3 par conférence:")
        
        for conf in ['East', 'West']:
            conf_top3 = df[df['Conference'] == conf].nlargest(3, 'Win%')[['FullTeamName', 'W', 'L', 'Win%']]
            print(f"\n{conf}:")
            print(conf_top3.to_string(index=False))
            
# Exemple pour obtenir les classements de 2020 à 2023
start_year = 1985
end_year = 1999

# Récupération et sauvegarde des classements dans des fichiers séparés
get_and_save_standings(start_year, end_year)

# # Analyse des classements par année
# analyze_standings_by_year()