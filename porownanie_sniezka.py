import pandas as pd
from io import StringIO

xls = pd.ExcelFile("s_m_d_sniezka_dane_IMGW.xlsx")
frames = []
for sheet in xls.sheet_names:
    raw = pd.read_excel(xls, sheet_name=sheet, header=None)
    # Każdy wiersz to 1 linia CSV
    text = "\n".join(raw[0].astype(str))
    df = pd.read_csv(StringIO(text), sep=",", quotechar='"', header=None)
    df = df[[2, 3, 12]]                 # year, month, tmean
    df.columns = ["year", "month", "tmean_imgw"]
    df["year"] = df["year"].astype(int)
    df["month"] = df["month"].astype(int)
    frames.append(df)

imgw_clean = pd.concat(frames, ignore_index=True)

grid = pd.read_csv("dane_pogodowe_miesiecznie/miesiac_SNIEZKA_2020_2024.csv")
merged = grid.merge(imgw_clean, on=["year","month"])

merged["diff"] = merged["temperature_2m_mean"] - merged["tmean_imgw"]

print(merged[["year","month","temperature_2m_mean","tmean_imgw","diff"]])
print("\nŚrednia różnica:", merged["diff"].mean())
print("RMSE:", (merged["diff"]**2).mean()**0.5)