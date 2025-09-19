import pandas as pd
import requests
import time
from pathlib import Path

# === Parametry ===
start_date = "2020-01-01"
end_date = "2024-12-31"
timezone = "Europe/Warsaw"
params = [
    "temperature_2m_max",
    "temperature_2m_min",
    "temperature_2m_mean",
    "precipitation_sum",
    "windspeed_10m_max",
    "weathercode",
    "snowfall_sum",
    "sunshine_duration",
    "cloudcover_mean"
]

# === Wczytaj współrzędne szczytów ===
koordynaty_path = "koordynaty.csv"  # Upewnij się, że ten plik jest w tym samym katalogu
df_coords = pd.read_csv(koordynaty_path)

# === Stwórz folder na dane pogodowe ===
output_dir = Path("dane_pogodowe")
output_dir.mkdir(exist_ok=True)

# === Pobieranie danych ===
for idx, row in df_coords.iterrows():
    nazwa = row["nazwa"]
    szczyt_id = row["id_szczytu"]
    lat = row["lat"]
    lon = row["lon"]
    output_file = output_dir / f"pogoda_{szczyt_id}_2020_2024.csv"

    # Pomiń pobieranie dla tego szczytu jeśli plik z danymi już istnieje
    if output_file.exists():
        continue

    print(f"Pobieram dane dla: {nazwa} ({lat}, {lon})...")

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={lon}"
        f"&start_date={start_date}&end_date={end_date}"
        f"&daily=" + ",".join(params) +
        f"&timezone={timezone}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        df = pd.DataFrame(data["daily"])
        df["location"] = szczyt_id

        output_file = output_dir / f"pogoda_{szczyt_id}_2020_2024.csv"
        df.to_csv(output_file, index=False)
        print(f"Zapisano: {output_file.name}")

    except Exception as e:
        print(f"Błąd dla {nazwa}: {e}")

    # Krótka przerwa dla bezpieczeństwa (API rate limit)
    time.sleep(3)

print("\nPobieranie zakończone!")