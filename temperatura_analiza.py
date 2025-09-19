import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from grupowanie_szczytow import peak_to_region, peak_to_altitude_group, clean_peak_name

# --- 1. Wczytanie danych ---
input_dir = Path("dane_pogodowe_miesiecznie")
files = list(input_dir.glob("miesiac_*.csv"))
frames = []

for file in files:
    df = pd.read_csv(file)
    # wyciągamy nazwę szczytu z pliku i czyścimy
    peak_name = file.stem.replace("miesiac_", "").replace("_2020_2024", "")
    peak_name = clean_peak_name(peak_name)  # <- normalizacja z polskimi znakami
    df["peak"] = peak_name
    frames.append(df)

data = pd.concat(frames, ignore_index=True)

# --- 2. Dodajemy regiony i grupy wysokościowe ---
data["region"] = data["peak"].map(peak_to_region)
data["altitude_group"] = data["peak"].map(peak_to_altitude_group)
data["month"] = data["month"].astype(int)  # upewniamy się, że miesiąc to liczba

# --- 3. Analizy temperatury ---

# Średnie miesięczne temperatury (dla każdego szczytu)
avg_monthly = (
    data.groupby(["peak", "month"])["temperature_2m_mean"]
    .mean()
    .reset_index()
)

# Amplituda roczna dla każdego szczytu
amplitude = (
    data.groupby("peak")["temperature_2m_mean"]
    .agg(lambda x: x.groupby(data["month"]).mean().max() - x.groupby(data["month"]).mean().min())
)

# Liczba miesięcy >10°C (średnia dla lat 2020–2024)
warm_counts = (
    data.groupby(["peak", "year", "month"])["temperature_2m_mean"]
    .mean()
    .reset_index()
)
warm_counts = (
    warm_counts.groupby(["peak", "year"])["temperature_2m_mean"]
    .apply(lambda x: (x > 10).sum())
    .groupby("peak")
    .mean()
)

# --- 4. Wizualizacje ---

# Wykres: średnia miesięczna wg grup wysokościowych
avg_monthly_alt = (
    data.groupby(["altitude_group", "month"])["temperature_2m_mean"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(8,5))
for group in avg_monthly_alt["altitude_group"].unique():
    subset = avg_monthly_alt[avg_monthly_alt["altitude_group"] == group]
    plt.plot(
        subset["month"], subset["temperature_2m_mean"],
        label=group, marker="o"
    )

plt.title("Średnia miesięczna temperatura (2020–2024) wg grup wysokościowych", fontsize=13)
plt.xlabel("Miesiąc", fontsize=11)
plt.ylabel("Temperatura [°C]", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.ylim(-15, 20)
plt.show()

# Wykres: średnia miesięczna wg regionów
avg_monthly_region = (
    data.groupby(["region", "month"])["temperature_2m_mean"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(8,5))
for region in avg_monthly_region["region"].dropna().unique():
    subset = avg_monthly_region[avg_monthly_region["region"] == region]
    plt.plot(
        subset["month"], subset["temperature_2m_mean"],
        label=region, marker="o"
    )

plt.title("Średnia miesięczna temperatura (2020–2024) wg regionów", fontsize=13)
plt.xlabel("Miesiąc", fontsize=11)
plt.ylabel("Temperatura [°C]", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.ylim(-15, 20)
plt.show()

# --- 5. Podsumowanie tabelaryczne ---
print("Amplituda roczna temperatur (°C):")
print(amplitude.sort_values(ascending=False))

print("\nŚrednia liczba miesięcy >10°C:")
print(warm_counts.sort_values(ascending=False))

# --- 5. Zapis wyników do plików ---

# amplituda do DataFrame
amplitude_df = amplitude.reset_index().rename(columns={"temperature_2m_mean": "amplitude"})
# liczba miesięcy >10°C do DataFrame
warm_counts_df = warm_counts.reset_index().rename(columns={"temperature_2m_mean": "months_above_10C"})

# zapis do Excela (dwa arkusze)
with pd.ExcelWriter("analiza_temperatur.xlsx") as writer:
    amplitude_df.to_excel(writer, sheet_name="Amplituda", index=False)
    warm_counts_df.to_excel(writer, sheet_name="Miesiace>10C", index=False)

# zapis do CSV (osobne pliki)
amplitude_df.to_csv("amplituda_temperatur.csv", index=False)
warm_counts_df.to_csv("miesiace_pow_10C.csv", index=False)

print("✅ Wyniki zapisane do 'analiza_temperatur.xlsx' oraz CSV.")


data = pd.concat(frames, ignore_index=True)

# --- Test poprawności nazw szczytów ---
unique_peaks = sorted(data["peak"].unique())
print("\n✅ Unikalne szczyty po normalizacji (powinno być 28):")
for p in unique_peaks:
    print("-", p)

print(f"\nLiczba unikalnych szczytów: {len(unique_peaks)}\n")


