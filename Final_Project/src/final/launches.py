# src/final/launches.py
import requests
import pandas as pd

def fetch_all_launches(base_url, params):
    """
    Fetch all launches from Launch Library 2 API within given parameters.
    Handles pagination automatically.
    """
    all_launches = []
    url = base_url
    current_params = params.copy()
    
    while url:
        response = requests.get(url, params=current_params)
        response.raise_for_status()

        data = response.json()
        launches = data.get("results", [])
        all_launches.extend(launches)
        
        next_url = data.get("next")
        if next_url:
            url = next_url
            current_params = None
        else:
            break
    return all_launches

def parse_launch_data(launches):
    """
    Parse raw launch data into a DataFrame.
    """
    records = []
    for launch in launches:
        provider = launch.get("launch_service_provider", {}).get("name")
        pad = launch.get("pad", {})
        launch_site_name = pad.get("name")
        launch_site_location = pad.get("location", {}).get("name")

        mission = launch.get("mission", {})
        orbit = mission.get("orbit") if isinstance(mission, dict) else None

        records.append({
            "launch_id": launch.get("id"),
            "name": launch.get("name"),
            "status": launch.get("status", {}).get("name"),
            "window_start": launch.get("window_start"),
            "window_end": launch.get("window_end"),
            "provider": provider,
            "launch_site_name": launch_site_name,
            "launch_site_location": launch_site_location,
            "orbit": orbit
        })
    return pd.DataFrame(records)
