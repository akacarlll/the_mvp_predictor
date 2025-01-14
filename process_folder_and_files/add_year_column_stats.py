import os
import pandas as pd

def process_and_save_individual_files(folder_path, output_folder):
    """
    Charge chaque fichier CSV dans un dossier, ajoute une colonne 'année' basée sur le nom du fichier,
    et sauvegarde le fichier modifié.

    Parameters:
    - folder_path (str): Chemin vers le dossier contenant les fichiers CSV.
    - output_folder (str): Chemin vers le dossier où enregistrer les fichiers modifiés.

    Returns:
    - None
    """
    # Créer le dossier de destination s'il n'existe pas
    os.makedirs(output_folder, exist_ok=True)

    # Parcourir tous les fichiers dans le dossier
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):  # Vérifie que le fichier est un CSV
            file_path = os.path.join(folder_path, filename)
            
            # Lire le fichier CSV
            df = pd.read_csv(file_path)
            
            # Extraire l'année du nom de fichier (e.g., "stat_per_game_1980.csv" -> 1980)
            year = int(filename.split('_')[-1].split('.')[0])
            
            # Ajouter la colonne 'année'
            df['Year'] = year
            
            # Définir le chemin de sortie pour le fichier modifié
            output_file_path = os.path.join(output_folder, filename)
            
            # Sauvegarder le fichier modifié
            df.to_csv(output_file_path, index=False)
            print(f"Fichier traité et sauvegardé : {output_file_path}")

# Exemple d'utilisation
folder_path = r"C:\Users\carlf\Documents\GitHub\The_Great_MVP_Predictor\stats_csv"
output_folder = r"C:\Users\carlf\Documents\GitHub\The_Great_MVP_Predictor\stats_csv"

# Appeler la fonction
process_and_save_individual_files(folder_path, output_folder)