# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --- Ścieżki ---
file_path = Path(r"D:\Programowanie\analiza-pogodowa-KGP") / "kgp_all_monthly_clean.csv"
plots_dir = Path("plots/peaks"); plots_dir.mkdir(parents=True, exist_ok=True)
tables_dir = Path("tables/peaks"); tables_dir.mkdir(parents=True, exist_ok=True)

# --- Wczytanie danych ---
df = pd.read_csv(file_path)

# --- Etykiety miesięcy ---
m_labels = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"]

# --- Jednostki ---
units = {
    "temperature_2m_mean": "°C",
    "precipitation_sum": "mm",
    "snowfall_sum": "mm",
    "windspeed_10m_max": "m/s",
    "cloudcover_mean": "%",
    "sunshine_duration": "h"
}

# --- Funkcja do znajdowania ekstremów ---
def extremum_row(df_m, col, how="max"):
    s = df_m[col].dropna()
    if s.empty:
        return {"month": None, col: None}
    idx = s.idxmax() if how=="max" else s.idxmin()
    return {"month": int(df_m.loc[idx, "month"]), col: float(df_m.loc[idx, col])}

# --- Funkcja główna ---
def analyze_peak(peak_name, df):
    df_peak = df[df["Szczyt"] == peak_name].copy()
    if df_peak.empty:
        print(f"⚠ Brak danych dla: {peak_name}")
        return

    # Agregacja miesięczna (średnia z lat)
    cols = list(units.keys())
    monthly = df_peak.groupby("month", as_index=False)[cols].mean()

    # --- Wykres 2×3 ---
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    fig.suptitle(f"Sezonowość warunków — {peak_name}", fontsize=16)

    plot_vars = [
        ("temperature_2m_mean", "Średnia temperatura"),
        ("precipitation_sum", "Suma opadów"),
        ("snowfall_sum", "Opady śniegu"),
        ("windspeed_10m_max", "Maks. prędkość wiatru"),
        ("cloudcover_mean", "Średnie zachmurzenie"),
        ("sunshine_duration", "Czas nasłonecznienia"),
    ]

    for ax, (col, title) in zip(axes.flat, plot_vars):
        ax.plot(monthly["month"], monthly[col], marker="o")
        ax.set_title(title, fontsize=11)
        ax.set_xticks(range(1,13))
        ax.set_xticklabels(m_labels)
        ax.set_ylabel(units[col])
        ax.grid(alpha=0.3)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(plots_dir / f"{peak_name}_all.png")
    plt.close()

    # --- Ekstrema ---
    summary_items = {
        "Najzimniejszy miesiąc": extremum_row(monthly, "temperature_2m_mean", "min"),
        "Najcieplejszy miesiąc": extremum_row(monthly, "temperature_2m_mean", "max"),
        "Najbardziej deszczowy": extremum_row(monthly, "precipitation_sum", "max"),
        "Najmniej deszczowy":   extremum_row(monthly, "precipitation_sum", "min"),
        "Najbardziej śnieżny":  extremum_row(monthly, "snowfall_sum", "max"),
        "Najbardziej wietrzny": extremum_row(monthly, "windspeed_10m_max", "max"),
        "Najbardziej pochmurny": extremum_row(monthly, "cloudcover_mean", "max"),
        "Najbardziej słoneczny": extremum_row(monthly, "sunshine_duration", "max"),
        "Najmniej słoneczny":   extremum_row(monthly, "sunshine_duration", "min"),
    }

    # --- Raport tekstowy ---
    def month_label(m): return m_labels[m-1] if m else "-"

    report_lines = [f"Raport dla szczytu: {peak_name}\n"]
    for k, v in summary_items.items():
        m = month_label(v.get("month"))
        col = [kk for kk in v.keys() if kk != "month"][0]
        val = v[col]
        if isinstance(val, float):
            val = round(val, 2)
        unit = units.get(col, "")
        report_lines.append(f"{k}: {m}, {val} {unit}")

    report_text = "\n".join(report_lines)

    with open(tables_dir / f"{peak_name}_report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)

    print(report_text)

# --- Uruchomienie dla wszystkich szczytów ---
for peak in df["Szczyt"].unique():
    analyze_peak(peak, df)
