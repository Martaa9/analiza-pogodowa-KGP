# --- Grupowanie szczytów KGP ---

# Przypisanie szczytów do regionów górskich
peak_to_region = {
    # Tatry
    "Rysy": "Tatry",

    # Sudety
    "Śnieżka": "Sudety",
    "Śnieżnik": "Sudety",
    "Wysoka Kopa": "Sudety",
    "Ślęża": "Sudety",
    "Szczeliniec Wielki": "Sudety",
    "Jagodna": "Sudety",
    "Orlica": "Sudety",
    "Wielka Sowa": "Sudety",
    "Kłodzka Góra": "Sudety",
    "Kowadło": "Sudety",
    "Czarna Góra": "Sudety",
    "Rudawiec": "Sudety",
    "Skalnik": "Sudety",
    "Skopiec": "Sudety",
    "Biskupia Kopa": "Sudety",
    "Chełmiec": "Sudety",
    "Waligóra": "Sudety",

    # Beskidy Zachodnie
    "Babia Góra": "Beskidy Zachodnie",
    "Pilsko": "Beskidy Zachodnie",
    "Wielka Racza": "Beskidy Zachodnie",
    "Skrzyczne": "Beskidy Zachodnie",
    "Turbacz": "Beskidy Zachodnie",
    "Mogielica": "Beskidy Zachodnie",
    "Radziejowa": "Beskidy Zachodnie",
    "Lubomir": "Beskidy Zachodnie",
    "Czupel": "Beskidy Zachodnie",

    # Beskidy Wschodnie
    "Tarnica": "Beskidy Wschodnie",
    "Lackowa": "Beskidy Wschodnie",

    # Góry Świętokrzyskie
    "Łysica": "Góry Świętokrzyskie",
}

# Przypisanie szczytów do kategorii wysokościowych
peak_to_altitude_group = {
    # Niskie <1000 m
    "Łysica": "Niskie",
    "Ślęża": "Niskie",
    "Kłodzka Góra": "Niskie",
    "Lubomir": "Niskie",
    "Szczeliniec Wielki": "Niskie",
    "Jagodna": "Niskie",
    "Kowadło": "Niskie",
    "Lackowa": "Niskie",
    "Czupel": "Niskie",
    "Biskupia Kopa": "Niskie",
    "Chełmiec": "Niskie",
    "Waligóra": "Niskie",
    "Skalnik": "Niskie",
    "Skopiec": "Niskie",

    # Średnie 1000–1500 m
    "Orlica": "Średnie",
    "Wielka Sowa": "Średnie",
    "Wysoka Kopa": "Średnie",
    "Rudawiec": "Średnie",
    "Mogielica": "Średnie",
    "Czarna Góra": "Średnie",
    "Skrzyczne": "Średnie",
    "Radziejowa": "Średnie",
    "Wysoka (Pieniny)": "Średnie",
    "Turbacz": "Średnie",
    "Tarnica": "Średnie",
    "Wielka Racza": "Średnie",

    # Wysokie >1500 m
    "Babia Góra": "Wysokie",
    "Pilsko": "Wysokie",
    "Śnieżka": "Wysokie",
    "Śnieżnik": "Wysokie",
    "Rysy": "Wysokie",
}

# --- Funkcja czyszcząca nazwy szczytów z plików CSV ---
def clean_peak_name(name: str) -> str:
    """
    Normalizuje nazwy szczytów KGP do poprawnej formy (z polskimi znakami).
    Obsługuje uproszczone nazwy z plików CSV.
    """
    normalize_names = {
        "LYSICA": "Łysica",
        "SLEZA": "Ślęża",
        "KLODZKA GORA": "Kłodzka Góra",
        "LUBOMIR": "Lubomir",
        "SZCZELINIEC": "Szczeliniec Wielki",
        "JAGODNA": "Jagodna",
        "KOWADLO": "Kowadło",
        "LACKOWA": "Lackowa",
        "CZUPEL": "Czupel",
        "BISKUPIA KOPA": "Biskupia Kopa",
        "CHELMIEC": "Chełmiec",
        "WALIGORA": "Waligóra",
        "SKALNIK": "Skalnik",
        "SKOPIEC": "Skopiec",
        "ORLICA": "Orlica",
        "WIELKA SOWA": "Wielka Sowa",
        "WYSOKA KOPA": "Wysoka Kopa",
        "RUDAWIEC": "Rudawiec",
        "MOGIELICA": "Mogielica",
        "SKRZYCZNE": "Skrzyczne",
        "RADZIEJOWA": "Radziejowa",
        "WYSOKA PIENINY": "Wysoka (Pieniny)",
        "TURBACZ": "Turbacz",
        "TARNICA": "Tarnica",
        "WIELKA RACZA": "Wielka Racza",
        "BABIA GORA": "Babia Góra",
        "SNIEZKA": "Śnieżka",
        "RYSY": "Rysy",
        "SNIEZNIK": "Śnieżnik"   # dodatkowo – nie jest w oficjalnej KGP
    }

    # ujednolicamy wejście: wielkie litery + spacje zamiast podkreśleń
    name = name.upper().replace("_", " ")

    # zwracamy poprawną nazwę, jeśli jest w słowniku
    return normalize_names.get(name, name)




