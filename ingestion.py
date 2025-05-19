import json
from typing import List
from pydantic import BaseModel


class ServiceStatus(BaseModel):
    database: str
    api_gateway: str
    cache: str


class MonitoringData(BaseModel):
    timestamp: str
    cpu_usage: float
    memory_usage: float
    latency_ms: float
    disk_usage: float
    network_in_kbps: float
    network_out_kbps: float
    io_wait: float
    thread_count: int
    active_connections: int
    error_rate: float
    uptime_seconds: int
    temperature_celsius: float
    power_consumption_watts: float
    service_status: ServiceStatus


def load_data(filepath: str) -> List[MonitoringData]:
    with open(filepath, "r") as f:
        raw_data = json.load(f)
    return [MonitoringData(**entry) for entry in raw_data]
