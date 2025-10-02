import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- dane ---
df = pd.read_csv(r"D:\Programowanie\analiza-pogodowa-KGP\kgp_all_monthly_clean.csv")

# --- grupowanie: średnia miesięczna w regionach ---
region_monthly = (
    df.groupby(["region", "month"])
    [["temperature_2m_mean", "precipitation_sum"]]
    .mean()
    .reset_index()
)

# --- grupowanie: średnia miesięczna w grupach wysokościowych ---
height_monthly = (
    df.groupby(["height_group", "month"])
    [["temperature_2m_mean", "precipitation_sum"]]
    .mean()
    .reset_index()
)

# palety
region_colors = {
    "Tatry": "#08306b",
    "Sudety": "#1b9e77",
    "Beskidy": "#2171b5",
    "Bieszczady": "#7570b3",
    "Pieniny": "#66c2a5",
    "Góry Świętokrzyskie": "#a6d854"
}

height_colors = {
    "Wysokie": "#7570b3",
    "Średnie": "#66c2a5",
    "Niskie": "#a6d854"
}

# --- folder wyjściowy ---
output_combined = r"D:\Programowanie\analiza-pogodowa-KGP\plots\combined"
os.makedirs(output_combined, exist_ok=True)

# --- 4 wykresy w jednej tablicy ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Regiony – temperatura
sns.lineplot(
    data=region_monthly,
    x="month", y="temperature_2m_mean",
    hue="region", marker="o", palette=region_colors,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Średnia miesięczna temperatura – regiony")
axes[0, 0].set_xlabel("Miesiąc")
axes[0, 0].set_ylabel("°C")
axes[0, 0].grid(alpha=0.3)

# 2. Regiony – opady
sns.lineplot(
    data=region_monthly,
    x="month", y="precipitation_sum",
    hue="region", marker="o", palette=region_colors,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Średnie miesięczne opady – regiony")
axes[0, 1].set_xlabel("Miesiąc")
axes[0, 1].set_ylabel("mm")
axes[0, 1].grid(alpha=0.3)

# 3. Grupy wysokościowe – temperatura
sns.lineplot(
    data=height_monthly,
    x="month", y="temperature_2m_mean",
    hue="height_group", marker="o", palette=height_colors,
    hue_order=["Wysokie", "Średnie", "Niskie"],
    ax=axes[1, 0]
)
axes[1, 0].set_title("Średnia miesięczna temperatura – grupy wysokościowe")
axes[1, 0].set_xlabel("Miesiąc")
axes[1, 0].set_ylabel("°C")
axes[1, 0].grid(alpha=0.3)

# 4. Grupy wysokościowe – opady
sns.lineplot(
    data=height_monthly,
    x="month", y="precipitation_sum",
    hue="height_group", marker="o", palette=height_colors,
    hue_order=["Wysokie", "Średnie", "Niskie"],
    ax=axes[1, 1]
)
axes[1, 1].set_title("Średnie miesięczne opady – grupy wysokościowe")
axes[1, 1].set_xlabel("Miesiąc")
axes[1, 1].set_ylabel("mm")
axes[1, 1].grid(alpha=0.3)

# układ legend
for ax in axes.flat:
    ax.legend(title="", fontsize=8)

plt.suptitle("Porównanie regionów i grup wysokościowych (2020–2024)", fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.97])

plt.savefig(os.path.join(output_combined, "regions_heights_comparison.png"), dpi=300)
plt.show()
