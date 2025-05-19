from ingestion import MonitoringData


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
