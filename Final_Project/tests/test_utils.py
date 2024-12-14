import pandas as pd
from final.utils import merge_data

def test_merge_data():
    neo_df = pd.DataFrame({
        "neo_id": ["1"],
        "name": ["Mock NEO"],
        "close_approach_date": ["2024-01-01"]
    })
    launch_df = pd.DataFrame({
        "launch_id": ["123"],
        "name": ["Mock Launch"],
        "window_start": ["2024-01-01"],
        "launch_site_location": ["Mock Location"]  # Added necessary column
    })
    site_df = pd.DataFrame({
        "Location": ["Mock Location"],
        "Country": ["Mock Country"],
        "Coordinates": ["0.0N, 0.0E"]
    })

    merged = merge_data(neo_df, launch_df, site_df)
    assert len(merged) == 1
    assert "launch_id" in merged.columns
    assert "neo_id" in merged.columns
    assert "Country" in merged.columns
