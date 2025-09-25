# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --- ścieżki ---
comfort_path = Path("tables/comfort/all_peaks_comfort.csv")
meta_path = Path("KGP_metadata.csv")  # w tym pliku: Szczyt, Wysokość (m n.p.m.), Grupa wysokościowa

# --- dane ---
df = pd.read_csv(comfort_path)
meta = pd.read_csv(meta_path)

# scal z metadanymi
df = df.merge(meta[["Szczyt", "Wysokość (m n.p.m.)", "Grupa wysokościowa"]], on="Szczyt", how="left")

# etykiety miesięcy
m_labels = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"]

# pivot + sortowanie wg wysokości
pivot = (
    df.pivot_table(index=["Szczyt","Wysokość (m n.p.m.)","Grupa wysokościowa"],
                   columns="month", values="ComfortScore")
      .reset_index()
      .sort_values("Wysokość (m n.p.m.)", ascending=True)
      .set_index("Szczyt")
      .drop(columns=["Wysokość (m n.p.m.)","Grupa wysokościowa"])
)
pivot = pivot.reindex(columns=range(1,13))
pivot.columns = m_labels

# adnotacje min i max
annot = pivot.copy().astype(str)
for idx, row in pivot.iterrows():
    min_idx = row.idxmin()
    max_idx = row.idxmax()
    for col in pivot.columns:
        annot.at[idx, col] = f"{int(row[col])}" if col in (min_idx, max_idx) else ""

# mapowanie grup wysokościowych -> neutralne kolory
group_map = dict(zip(meta["Szczyt"], meta["Grupa wysokościowa"]))
color_map = {
    "Niskie": "#6BAED6",   # jasnoniebieski
    "Średnie": "#2171B5",  # średni niebieski
    "Wysokie": "#08306B"    # ciemny granat
}

# rysowanie
plt.figure(figsize=(16,9))
ax = sns.heatmap(
    pivot,
    annot=annot, fmt="",
    cmap="YlGnBu",
    cbar_kws={'label': 'Comfort Score (0–100)'},
    linewidths=1,
    linecolor="white"
)

# kolorowanie etykiet Y wg grup
for label in ax.get_yticklabels():
    szczyt = label.get_text()
    group = group_map.get(szczyt, "")
    if group in color_map:
        label.set_color(color_map[group])
    else:
        label.set_color("black")

plt.title("Comfort Score — szczyty KGP", fontsize=16)
plt.xlabel("Miesiąc")
plt.ylabel("Szczyt")
plt.tight_layout()

Path("plots/comfort").mkdir(parents=True, exist_ok=True)
plt.savefig("plots/comfort/heatmap_all_peaks_colored.png")
plt.show()