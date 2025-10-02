import pandas as pd
import os

# --- dane ---
df = pd.read_csv(r"D:\Programowanie\analiza-pogodowa-KGP\kgp_all_monthly_clean.csv")

# --- średnie roczne dla każdego szczytu ---
annual_means = df.groupby("Szczyt").mean(numeric_only=True).reset_index()

# --- TOP N w każdej kategorii ---
def topN(col, ascending=False, n=5):
    return annual_means[["Szczyt", col]].sort_values(col, ascending=ascending).head(n)

rankings = {
    "Najbardziej deszczowe (mm)": topN("precipitation_sum", ascending=False, n=5),
    "Najbardziej śnieżne (mm)": topN("snowfall_sum", ascending=False, n=5),
    "Najbardziej wietrzne (m/s)": topN("windspeed_10m_max", ascending=False, n=5),
    "Najbardziej słoneczne (h)": topN("sunshine_duration", ascending=False, n=5),
    "Najbardziej pochmurne (%)": topN("cloudcover_mean", ascending=False, n=5),
    "Najcieplejsze (°C)": topN("temperature_2m_mean", ascending=False, n=5),
    "Najzimniejsze (°C)": topN("temperature_2m_mean", ascending=True, n=5),
}

# --- tworzenie tabeli Markdown ---
lines = []
lines.append("| Kategoria | 1 miejsce | 2 miejsce | 3 miejsce | 4 miejsce | 5 miejsce |")
lines.append("|-----------|-----------|-----------|-----------|-----------|-----------|")

for category, df_rank in rankings.items():
    places = [f"{row.Szczyt} ({getattr(row, df_rank.columns[1]):.1f})" for row in df_rank.itertuples()]
    lines.append(f"| {category} | {places[0]} | {places[1]} | {places[2]} | {places[3]} | {places[4]} |")

markdown_table = "\n".join(lines)

# --- zapis do pliku ---
output_path = r"D:\Programowanie\analiza-pogodowa-KGP\rankings.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(markdown_table)

print("Tabela rankingowa zapisana do:", output_path)
print(markdown_table)