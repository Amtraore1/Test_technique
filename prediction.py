from statistics import linear_regression

from ingestion import MonitoringData
from typing import List
import pandas as pd
import json


def detection_anomalies(data: MonitoringData) -> dict:
    anomalies = {}

    if data.cpu_usage > 80:
        anomalies['cpu_usage'] = f"CPU élevé ({data.cpu_usage}%)"
    if data.latency_ms > 200:
        anomalies['latency'] = f"Latence élevée ({data.latency_ms}ms)"
    if data.error_rate > 0.01:
        anomalies['error_rate'] = f"Taux d'erreur élevé ({data.error_rate})"
    if data.temperature_celsius > 70:
        anomalies['temperature'] = f"Température élevée ({data.temperature_celsius}°C)"
    if data.service_status.api_gateway != "online":
        anomalies['api_gateway'] = f"API Gateway en état '{data.service_status.api_gateway}'"

    return anomalies
def historique(data: list) -> dict:
    df=pd.dataframe([data.dict])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.sort_values('timestamp', inplace=True)
    df.set_index('timestamp', inplace=True)

tendance{}

for metric in ['cpu_usage', 'latency', 'error_rate', 'temperature_celsius', 'service_status']:
x=np.range[len(df)].reshape(-1, 1)
y=df[metric].values.reshape(-1, 1)
model=linear_regression().fit(x,y)
coef=model.coef_[0][0]

    if coef>0,1:
        tendance[metric]=f"tendances emergentes a la hausse detecté"
    if coef<0,1:
    tendance[metric]=f"tendances emergentes a la basse detecté"