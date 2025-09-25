# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# --- Ścieżki ---
file_path = Path(r"D:\Programowanie\analiza-pogodowa-KGP") / "kgp_all_monthly_clean.csv"
plots_dir = Path("plots/comfort")
plots_dir.mkdir(parents=True, exist_ok=True)
tables_dir = Path("tables/comfort")
tables_dir.mkdir(parents=True, exist_ok=True)

# --- Wczytanie danych ---
df = pd.read_csv(file_path)

# --- Etykiety miesięcy ---
m_labels = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]


# --- Funkcje pomocnicze ---
def pct_rank(s: pd.Series) -> pd.Series:
    """Percentyl rank w [0,1]; jeśli seria stała, zwraca 0.5"""
    if s.nunique(dropna=True) <= 1:
        return pd.Series(0.5, index=s.index)
    return s.rank(method="average", pct=True)


def temp_score(t):
    """Ocena temperatury (optimum 10–18 °C, 0 poza 0–25 °C)"""
    if pd.isna(t):
        return np.nan
    if t < 0 or t > 25:
        return 0.0
    if 10 <= t <= 18:
        return 1.0
    if t < 10:
        return (t - 0.0) / (10.0 - 0.0)  # 0 → 1
    else:  # 18 < t ≤ 25
        return (25.0 - t) / (25.0 - 18.0)  # 1 → 0


def comfort_score_monthly(df_peak, use_sun=True):
    """Liczy Comfort Score dla jednego szczytu"""
    cols = ["temperature_2m_mean", "precipitation_sum", "windspeed_10m_max"]
    if use_sun and "sunshine_duration" in df_peak.columns:
        cols.append("sunshine_duration")

    monthly = df_peak.groupby("month", as_index=False)[cols].mean()

    # Percentyle dla opadów, wiatru i słońca
    monthly["RainScore"] = 1 - pct_rank(monthly["precipitation_sum"])
    monthly["WindScore"] = 1 - pct_rank(monthly["windspeed_10m_max"])
    if use_sun and "sunshine_duration" in monthly:
        monthly["SunScore"] = pct_rank(monthly["sunshine_duration"])

    # Temperatura
    monthly["TempScore"] = monthly["temperature_2m_mean"].apply(temp_score)

    # Agregacja
    if use_sun:
        wT, wR, wW, wS = 0.35, 0.30, 0.20, 0.15
        cs = (wT * monthly["TempScore"] + wR * monthly["RainScore"] +
              wW * monthly["WindScore"] + wS * monthly["SunScore"])
    else:
        wT, wR, wW = 0.40, 0.35, 0.25
        cs = (wT * monthly["TempScore"] + wR * monthly["RainScore"] + wW * monthly["WindScore"])

    monthly["ComfortScore"] = (cs * 100).round(1)
    return monthly[["month", "ComfortScore", "TempScore", "RainScore", "WindScore"] + (["SunScore"] if use_sun else [])]


def plot_comfort(monthly, peak_name):
    """Wykres Comfort Score (barplot)"""
    plt.figure(figsize=(10, 4))
    plt.bar(monthly["month"], monthly["ComfortScore"], color="skyblue")
    plt.xticks(range(1, 13), m_labels)
    plt.ylabel("Comfort Score (0–100)")
    plt.title(f"Comfort Score — {peak_name}")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(plots_dir / f"{peak_name}_comfort.png")
    plt.close()


# --- Analiza dla wszystkich szczytów ---
all_results = []
for peak in df["Szczyt"].unique():
    df_peak = df[df["Szczyt"] == peak]
    monthly_cs = comfort_score_monthly(df_peak, use_sun=True)
    monthly_cs["Szczyt"] = peak
    all_results.append(monthly_cs)

    # zapis wykresu
    plot_comfort(monthly_cs, peak)
    # zapis csv
    monthly_cs.to_csv(tables_dir / f"{peak}_comfort.csv", index=False, encoding="utf-8")

# Zbiorczy plik CSV (wszystkie szczyty razem)
all_results_df = pd.concat(all_results, ignore_index=True)
all_results_df.to_csv("tables/comfort/all_peaks_comfort.csv", index=False, encoding="utf-8")

print("Gotowe — wykresy w plots/comfort/, CSV w tables/comfort/")

