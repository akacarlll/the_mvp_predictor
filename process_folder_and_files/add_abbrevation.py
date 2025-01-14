from nba_api.stats.static import teams
import pandas as pd
import os

def add_team_abbreviations(df=None, file_path=None):
    """
    Ajoute une colonne TEAM_ABBREVIATION au DataFrame ou au fichier CSV.
    
    Args:
        df (pandas.DataFrame, optional): DataFrame contenant les données
        file_path (str, optional): Chemin vers le fichier CSV
        
    Returns:
        pandas.DataFrame: DataFrame avec la nouvelle colonne TEAM_ABBREVIATION
    """
    # Récupération de toutes les équipes NBA et leurs abréviations
    nba_teams = teams.get_teams()
    
    # Création d'un dictionnaire de correspondance {nom complet: abréviation}
    team_abbrev_dict = {}
    for team in nba_teams:
        full_name = f"{team['city']} {team['nickname']}"
        team_abbrev_dict[full_name] = team['abbreviation']
    
    # Si un chemin de fichier est fourni, lire le CSV
    if file_path is not None:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Le fichier {file_path} n'existe pas")
        df = pd.read_csv(file_path)
    
    # Si aucun DataFrame n'est fourni après lecture du fichier
    if df is None:
        raise ValueError("Aucun DataFrame ou fichier valide n'a été fourni")
    
    # Création de la colonne TEAM_ABBREVIATION
    df['TEAM_ABBREVIATION'] = df['FullTeamName'].map(team_abbrev_dict)
    
    # Si certaines équipes n'ont pas été trouvées, afficher un avertissement
    missing_teams = df[df['TEAM_ABBREVIATION'].isna()]['FullTeamName'].unique()
    if len(missing_teams) > 0:
        print("Attention: Abréviations non trouvées pour les équipes:", missing_teams)
    
    # Si un fichier était fourni, sauvegarder les modifications
    if file_path is not None:
        df.to_csv(file_path, index=False)
        print(f"Fichier mis à jour : {file_path}")
    
    return df

# Fonction utilitaire pour traiter plusieurs fichiers dans un dossier
def add_abbreviations_to_folder(folder_path):
    """
    Ajoute les abréviations d'équipes à tous les fichiers CSV d'un dossier.
    
    Args:
        folder_path (str): Chemin vers le dossier contenant les fichiers CSV
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Le dossier {folder_path} n'existe pas")
    
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        print(f"\nTraitement du fichier : {file}")
        add_team_abbreviations(file_path=file_path)
        

# Pour traiter tous les fichiers CSV d'un dossier
add_abbreviations_to_folder("nba_standings")