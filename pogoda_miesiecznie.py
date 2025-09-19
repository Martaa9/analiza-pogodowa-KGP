import pandas as pd
from pathlib import Path

# Foldery
input_dir = Path("dane_pogodowe")
output_dir = Path("dane_pogodowe_miesiecznie")
output_dir.mkdir(exist_ok=True)

# Lista plików wejściowych
files = list(input_dir.glob("pogoda_*.csv"))

for file in files:
    df = pd.read_csv(file)
    szczyt_id = df["location"].iloc[0]

    # Konwersja daty
    df["time"] = pd.to_datetime(df["time"])
    df["year"] = df["time"].dt.year
    df["month"] = df["time"].dt.month

    # Agregacja miesięczna
    df_monthly = df.groupby(["year", "month"]).agg({
        "temperature_2m_max": "mean",
        "temperature_2m_min": "mean",
        "temperature_2m_mean": "mean",
        "precipitation_sum": "sum",
        "windspeed_10m_max": "mean",
        "snowfall_sum": "sum",
        "sunshine_duration": "mean",
        "cloudcover_mean": "mean"
    }).reset_index()

    # Dodaj nazwę szczytu
    df_monthly["location"] = szczyt_id

    # Zapis
    output_file = output_dir / f"miesiac_{szczyt_id}_2020_2024.csv"
    df_monthly.to_csv(output_file, index=False)
    print(f"Zapisano: {output_file.name}")

print("\nAgregacja miesięczna zakończona!")
