import pandas as pd

def merge_data(neo_df, launch_df, site_df):
    neo_df["close_approach_date"] = pd.to_datetime(neo_df["close_approach_date"])
    launch_df["window_start"] = pd.to_datetime(launch_df["window_start"]).dt.tz_localize(None)
    
    # Ensure all necessary columns are present before merging
    if "launch_site_location" not in launch_df.columns:
        launch_df["launch_site_location"] = "Unknown"
    
    merged = pd.merge(
        launch_df,
        neo_df,
        left_on="window_start",
        right_on="close_approach_date",
        how="outer"
    )
    final = pd.merge(
        merged,
        site_df,
        left_on="launch_site_location",
        right_on="Location",
        how="left"
    )
    return final
