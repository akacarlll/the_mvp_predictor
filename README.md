### NBA MVP Prediction Project 🏀
Ce projet vise à prédire le MVP (Most Valuable Player) de la NBA en exploitant un large éventail de données. Nous utilisons des techniques avancées de web scraping, de data engineering et de machine learning pour analyser les performances des joueurs au fil de la saison et fournir des insights exploitables via des visualisations interactives dans Power BI.

## 📊 Données collectées
Les données proviennent de plusieurs sources fiables :

Basketball Reference : statistiques détaillées des matchs (moyennes, boxscores, classements, etc.).
NBA.com : shot charts et autres métriques avancées.
Ballislife API : highlights et métriques complémentaires.

##🔧 Pipeline de traitement des données
Web Scraping :

Récupération automatisée des statistiques des joueurs et des équipes.
Mise à jour quotidienne des données dès qu'elles sont disponibles.
Feature Engineering :

Création de variables dérivées (efficacité, impact sur l'équipe, tendances de performance).
Intégration de données contextuelles (classements, adversaires, etc.).
Nettoyage et Transformation :

Standardisation des données pour les rendre exploitables dans les modèles de machine learning.
Gestion des valeurs manquantes et des incohérences.
Chargement dans Power BI :

Visualisation des performances des joueurs et des équipes.
Exploration des insights prédictifs grâce à des tableaux de bord interactifs.

## 🔍 Objectifs
Identifier les facteurs déterminants pour remporter le titre de MVP.
Explorer des visualisations avancées pour comparer les performances des candidats.
Tester des modèles prédictifs en utilisant des algorithmes de machine learning.
## 🚀 Technologies utilisées
Python : scraping et prétraitement des données (BeautifulSoup, pandas, scikit-learn).
API : intégration des données via des API tierces.
Kedro : pour gérer la pipeline de traitement des données.
Power BI : pour la visualisation des insights.

## 📈 Résultats attendus
Le projet vise à produire des prédictions fiables pour le MVP tout en offrant une vue d’ensemble des performances individuelles et collectives dans la NBA. Les tableaux de bord Power BI permettent aux utilisateurs de comprendre rapidement les dynamiques de la saison
