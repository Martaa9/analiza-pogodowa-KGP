import pandas as pd
from pathlib import Path

# --- Ścieżki ---
input_dir = Path(r"D:\Programowanie\analiza-pogodowa-KGP\dane_pogodowe_miesiecznie")
metadata_file = Path(r"D:\Programowanie\analiza-pogodowa-KGP\KGP_metadata.csv")
output_file = Path(r"D:\Programowanie\analiza-pogodowa-KGP\kgp_all_monthly_clean.csv")

# --- Wczytaj metadane (z kolumną NormName) ---
df_meta = pd.read_csv(metadata_file)
df_meta["NormName"] = df_meta["NormName"].str.strip()

# --- Wczytaj i scal pliki miesięczne ---
dfs = []
for file in input_dir.glob("miesiac_*.csv"):
    df = pd.read_csv(file)

    # nazwa techniczna z pliku (NormName)
    peak_norm = df['location'].iloc[0].strip()

    # dopasowanie do metadanych po NormName
    meta_row = df_meta[df_meta["NormName"] == peak_norm]
    if not meta_row.empty:
        df["ID"] = meta_row["ID"].values[0]
        df["Szczyt"] = meta_row["Szczyt"].values[0]
        df["NormName"] = meta_row["NormName"].values[0]
        df["height_m"] = meta_row["Wysokość (m n.p.m.)"].values[0]
        df["region"] = meta_row["Region"].values[0]
        df["height_group"] = meta_row["Grupa wysokościowa"].values[0]
    else:
        print(f"⚠️ Brak dopasowania dla '{peak_norm}' (plik {file.name})")
        df["ID"] = None
        df["Szczyt"] = peak_norm
        df["NormName"] = peak_norm
        df["height_m"] = None
        df["region"] = "Nieznany"
        df["height_group"] = "Brak"

    dfs.append(df)

# --- Scal wszystko ---
all_data = pd.concat(dfs, ignore_index=True)

# --- Usuń kolumnę location (bo mamy Szczyt + NormName) ---
all_data = all_data.drop(columns=["location"])

# --- Zapis do pliku ---
all_data.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"Scalono dane dla {all_data['Szczyt'].nunique()} szczytów.")
print(f"Plik zapisano jako: {output_file}")

