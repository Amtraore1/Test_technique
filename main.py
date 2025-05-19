from ingestion import load_data
from analyse import detection_anomalies
from recommendation import generate_recommendations
import json
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    mistral_api_key = os.getenv("MISTRAL_API_KEY")
    filepath = "data/rapport.json"

    print(" Ingestion des données...")
    dataset = load_data(filepath)

    full_report = []

    for data in dataset:
        anomalies = detection_anomalies(data)
        recommendations = generate_recommendations(anomalies, mistral_api_key)
        entry_report = {
            "timestamp": data.timestamp,
            "anomalies": anomalies,
            "recommendations": recommendations
        }
        full_report.append(entry_report)

    # Sauvegarde dans un fichier JSON
    with open("data/rapport_final.json", "w") as f:
        json.dump(full_report, f, indent=2, ensure_ascii=False)

    print("Rapport complet généré dans 'rapport_final.json'")

if __name__ == "__main__":
    main()
