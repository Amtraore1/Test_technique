from mistralai import Mistral
import os

def generate_recommendations(anomalies, api_key=None):
    if not anomalies:
        return ["Aucune anomalie détectée. Aucune recommandation nécessaire."]

    client = Mistral(api_key=api_key or os.getenv("MISTRAL_API_KEY"))
    model = "mistral-small-latest"

    prompt = (
        "Voici des anomalies techniques détectées sur un serveur :\n\n"
        + "\n".join(f"- {anomaly}" for anomaly in anomalies)
        + "\n\nDonne des recommandations précises et concrètes pour améliorer les performances."
        + "\n\nExploiter l’historique des données pour identifier les tendances émergentes"
    )

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = client.chat.complete(model=model, messages=messages)


    content = response.choices[0].message.content.strip()

    return content.split("\n")  # on retourne chaque ligne comme recommandation
