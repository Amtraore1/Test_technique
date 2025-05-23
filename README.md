# Optimisation d’Infrastructure et recommendation

## Objectif

Ce projet est une solution modulaire de monitoring et d’analyse d’infrastructure pour une PME. Il permet de :

- Ingestion de données système au format JSON  
- Détection d’anomalies (CPU, latence, etc.)  
- Génération de recommandations via le modèle LLM 
- Export des résultats dans un fichier json  

---

## Technologies Utilisées

| Outil / Lib         | Rôle |
|---------------------|------|
| Python 3.10     | Langage principal |
| `pydantic`           | Validation des données |
| `mistralai`          | Appel au modèle Mistral |
| `dotenv`             | Gestion des variables d'environnement |
| `json`               | Traitement des données |

---

##  Architecture du Projet
1- analyse.py # Détection des anomalies techniques   
2- ingestion.py # Lecture et validation des données JSON  
3- main.py # Pipeline principal  
4- recommendation.py # Appel à Mistral pour générer les recommandations  
5- data/  
    a-rapport.json # Données brutes d'entrée  
    b-rapport_final.json # Résultat final structuré  

---

##  Fonctionnement par Étapes

### Ingestion (ingestion.py)

Lit un fichier .json contenant les métriques système  
Valide les champs avec pydantic  

### Analyse (analyse.py)

Vérifie les valeurs au-delà des seuils critiques  
Retourne un dictionnaire des anomalies détectées  

### Recommandation (recommendation.py)

Formate un prompt avec les anomalies 
Utilise l’API mistralai pour interroger un modèle Mistral  
Retourne des recommandations ligne par ligne  

### Pipeline (main.py)

Gère l’exécution complète du processus  
Gère la lecture .env et sauvegarde le résultat final dans rapport_final.json  

##  pendant le test en présentiel
Pendant  le test en présentiel, j'ai voulu ajouter une nouvelle étape pour analyser l’historique des données (CPU, latence, erreurs, température, etc.).
Cette analyse utilise une régression linéaire pour détecter les tendances à la hausse ou à la baisse, ce qui permet d’anticiper les défaillances et d’optimiser la gestion des ressources.

Les résultats devront etre intégrés dans le prompt envoyé au LLM afin de proposer des recommandations plus précises et préventives.

##  Après le test en présentiel

Suite au test réalisé en présentiel, j’ai modifié le **prompt de génération** afin d'y intégrer une **analyse prédictive des tendances** basées sur l’historique des métriques.

-  **Avantage** : Très simple à implémenter (modification du prompt uniquement, sans changement d'architecture)
-  **Inconvénient** : Le traitement est **extrêmement long** (plus de 5 heures d'exécution) dû à la taille des données et la génération LLM séquentielle

📄 Le résultat de cette nouvelle version se trouve ici :  
`data/rapport_apres_test.json`
)
