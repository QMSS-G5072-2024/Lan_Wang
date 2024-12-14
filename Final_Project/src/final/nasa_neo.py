# src/final/nasa_neo.py
import requests
import pandas as pd

def fetch_neo_data(start_date, end_date, api_key):
    """
    Fetch NEO data from NASA's API for the given date range.

    Parameters
    ----------
    start_date : str
        Start date in YYYY-MM-DD
    end_date : str
        End date in YYYY-MM-DD
    api_key : str
        NASA API key

    Returns
    -------
    pd.DataFrame
        DataFrame of NEO data.
    """
    url = (
        f"https://api.nasa.gov/neo/rest/v1/feed"
        f"?start_date={start_date}&end_date={end_date}&api_key={api_key}"
    )
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    neo_dict = data.get("near_earth_objects", {})

    all_neos = []
    for date_key, neos in neo_dict.items():
        for neo in neos:
            is_hazardous = neo.get("is_potentially_hazardous_asteroid", False)
            approach_data = neo.get("close_approach_data", [])
            if approach_data:
                approach = approach_data[0]
                close_approach_date = approach.get("close_approach_date_full") or approach.get("close_approach_date")
                relative_velocity = approach.get("relative_velocity", {}).get("kilometers_per_second")
                miss_distance = approach.get("miss_distance", {}).get("kilometers")
                orbiting_body = approach.get("orbiting_body")
            else:
                close_approach_date = None
                relative_velocity = None
                miss_distance = None
                orbiting_body = None

            estimated_diameter = neo.get("estimated_diameter", {}).get("kilometers", {})
            est_dia_min = estimated_diameter.get("estimated_diameter_min")
            est_dia_max = estimated_diameter.get("estimated_diameter_max")

            all_neos.append({
                "neo_id": neo.get("id"),
                "name": neo.get("name"),
                "is_potentially_hazardous": is_hazardous,
                "close_approach_date": close_approach_date,
                "relative_velocity_km_s": relative_velocity,
                "miss_distance_km": miss_distance,
                "orbiting_body": orbiting_body,
                "estimated_diameter_min_km": est_dia_min,
                "estimated_diameter_max_km": est_dia_max
            })
    df = pd.DataFrame(all_neos)
    return df
