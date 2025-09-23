import pandas as pd

# --- słownik: wysokości szczytów ---
peak_heights = {
    "Łysica": 614,
    "Ślęża": 718,
    "Kłodzka Góra": 757,
    "Lubomir": 912,
    "Szczeliniec Wielki": 919,
    "Jagodna": 977,
    "Kowadło": 989,
    "Lackowa": 997,
    "Czupel": 930,
    "Biskupia Kopa": 889,
    "Chełmiec": 851,
    "Waligóra": 936,
    "Skalnik": 945,
    "Skopiec": 724,
    "Orlica": 1084,
    "Wielka Sowa": 1015,
    "Wysoka Kopa": 1126,
    "Rudawiec": 1106,
    "Mogielica": 1171,
    "Skrzyczne": 1257,
    "Radziejowa": 1266,
    "Wysoka (Pieniny)": 1050,
    "Turbacz": 1310,
    "Tarnica": 1346,
    "Babia Góra": 1725,
    "Śnieżka": 1603,
    "Śnieżnik": 1425,
    "Rysy": 2499,
}

# --- słownik: regiony geograficzne ---
peak_to_region = {
    "Łysica": "Góry Świętokrzyskie",
    "Ślęża": "Sudety",
    "Kłodzka Góra": "Sudety",
    "Lubomir": "Beskid Makowski",
    "Szczeliniec Wielki": "Sudety",
    "Jagodna": "Sudety",
    "Kowadło": "Sudety",
    "Lackowa": "Beskid Niski",
    "Czupel": "Beskid Mały",
    "Biskupia Kopa": "Sudety",
    "Chełmiec": "Sudety",
    "Waligóra": "Sudety",
    "Skalnik": "Sudety",
    "Skopiec": "Sudety",
    "Orlica": "Sudety",
    "Wielka Sowa": "Sudety",
    "Wysoka Kopa": "Sudety",
    "Rudawiec": "Sudety",
    "Mogielica": "Beskid Wyspowy",
    "Skrzyczne": "Beskid Śląski",
    "Radziejowa": "Beskid Sądecki",
    "Wysoka (Pieniny)": "Pieniny",
    "Turbacz": "Gorce",
    "Tarnica": "Bieszczady",
    "Babia Góra": "Beskid Żywiecki",
    "Śnieżka": "Sudety",
    "Śnieżnik": "Sudety",
    "Rysy": "Tatry",
}

# --- funkcja: grupy wysokościowe ---
def assign_altitude_group(height: int) -> str:
    if height < 1000:
        return "Niskie"
    elif height < 1500:
        return "Średnie"
    else:
        return "Wysokie"

# --- funkcja: NormName zgodne z plikami pogodowymi ---
def clean_peak_name(name: str) -> str:
    normalize_names = {
        "Łysica": "LYSICA",
        "Ślęża": "SLEZA",
        "Kłodzka Góra": "KLODZKA_GORA",
        "Lubomir": "LUBOMIR",
        "Szczeliniec Wielki": "SZCZELINIEC",
        "Jagodna": "JAGODNA",
        "Kowadło": "KOWADLO",
        "Lackowa": "LACKOWA",
        "Czupel": "CZUPEL",
        "Biskupia Kopa": "BISKUPIA_KOPA",
        "Chełmiec": "CHELMIEC",
        "Waligóra": "WALIGORA",
        "Skalnik": "SKALNIK",
        "Skopiec": "SKOPIEC",
        "Orlica": "ORLICA",
        "Wielka Sowa": "WIELKA_SOWA",
        "Wysoka Kopa": "WYSOKA_KOPA",
        "Rudawiec": "RUDAWIEC",
        "Mogielica": "MOGIELICA",
        "Skrzyczne": "SKRZYCZNE",
        "Radziejowa": "RADZIEJOWA",
        "Wysoka (Pieniny)": "WYSOKA_PIENINY",
        "Turbacz": "TURBACZ",
        "Tarnica": "TARNICA",
        "Babia Góra": "BABIA_GORA",
        "Śnieżka": "SNIEZKA",
        "Śnieżnik": "SNIEZNIK",
        "Rysy": "RYSY",
    }
    return normalize_names.get(name, name.upper())

# --- eksport metadanych ---
if __name__ == "__main__":
    df_meta = pd.DataFrame([
        {
            "Szczyt": peak,
            "Wysokość (m n.p.m.)": peak_heights[peak],
            "Region": peak_to_region[peak],
            "Grupa wysokościowa": assign_altitude_group(peak_heights[peak]),
            "NormName": clean_peak_name(peak),  # 👈 kolumna zgodna z plikami pogodowymi
        }
        for peak in peak_heights.keys()
    ])
    df_meta = df_meta.sort_values("Szczyt").reset_index(drop=True)
    df_meta.insert(0, "ID", df_meta.index + 1)

    df_meta.to_excel("KGP_metadata.xlsx", index=False)
    df_meta.to_csv("KGP_metadata.csv", index=False, encoding="utf-8-sig")

    print("✅ Zapisano KGP_metadata.xlsx oraz CSV (28 szczytów).")




