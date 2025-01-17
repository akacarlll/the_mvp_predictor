import os
import pandas as pd

def clean_and_add_year(folder_path):
    """
    Parcourt tous les fichiers CSV dans un dossier, supprime les lignes où la colonne RK == 'RK', 
    et ajoute une colonne YEAR basée sur le nom du fichier.

    Arguments :
        folder_path (str) : Chemin du dossier contenant les fichiers CSV.
    """
    # Parcourir tous les fichiers dans le dossier
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            try:
                # Charger le fichier CSV
                df = pd.read_csv(file_path)

                # # Supprimer les lignes où la colonne 'RK' vaut 'RK'
                df = df[df['RK'] != 'RK']

                # # Extraire l'année du nom du fichier
                year = int(filename.split('_')[-1].split('.')[0])

                # # Ajouter la colonne YEAR
                df['YEAR'] = year
                
                 # Séparer la colonne NAME en deux colonnes : NAME et Pos
                if 'NAME' in df.columns:
                    df['Pos'] = df['NAME'].str.split(',', expand=False).str[1].str.strip()
                    df['NAME'] = df['NAME'].str.split(',', expand=False).str[0].str.strip()


                # Sauvegarder le fichier nettoyé
                df.to_csv(file_path, index=False)
                print(f"Fichier nettoyé et mis à jour : {filename}")
            except Exception as e:
                print(f"Erreur avec le fichier {filename}: {e}")

# Chemin du dossier contenant les fichiers CSV
folder_path = r'C:\Users\carlf\Documents\GitHub\The_Great_MVP_Predictor\data\players_salaries'
clean_and_add_year(folder_path)