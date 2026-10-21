# Analiza warunków pogodowych Korony Gór Polski (2020–2024)

# Opis projektu

Projekt obejmuje analizę warunków pogodowych na 28 szczytach Korony Gór Polski (KGP) w latach 2020–2024. Na podstawie danych z Open-Meteo, przetworzonych i przeanalizowanych w Pythonie, porównano temperaturę, opady, wiatr, zachmurzenie i nasłonecznienie w różnych regionach i grupach wysokościowych.

Celem projektu było zbadanie sezonowości warunków pogodowych, wskazanie szczytów o najbardziej wymagających warunkach oraz określenie miesięcy sprzyjających górskim wędrówkom.

Wyniki przedstawiono na wykresach w Pythonie oraz w dashboardzie Power BI.

# Cele analizy

1. Zbadanie sezonowych zmian temperatur, opadów i pozostałych parametrów pogodowych.
2. Porównanie warunków pogodowych pomiędzy szczytami, regionami i grupami wysokościowymi.
3. Wskazanie szczytów o najbardziej wymagających warunkach.
4. Ocena, które miesiące mogą oferować najkorzystniejsze warunki do górskich wędrówek.

# Dane

- Źródło: Open-Meteo API
- Okres analizy: 2020–2024
- Zakres: 28 szczytów Korony Gór Polski
- Agregacja: dane dobowe przekształcone do wartości miesięcznych
- Zmienne: średnia, minimalna i maksymalna temperatura dobowa (°C), suma opadów (mm), opad śniegu (cm), maksymalna dobowa prędkość wiatru (km/h), czas nasłonecznienia i zachmurzenie (%)

Dane Open-Meteo mają charakter siatkowy, co oznacza, że wartości pogodowe są wyznaczane na podstawie interpolacji z modeli numerycznych w regularnych punktach siatki, a nie pochodzą bezpośrednio ze stacji pomiarowych, co może wpływać na ich dokładność.
Dla Śnieżki, jedynego szczytu KGP na którym znajduje się obserwatorium meteorologiczne, przeprowadzono porównanie danych siatkowych Open-Meteo z danymi stacyjnymi IMGW. W badanym okresie średnia różnica wyniosła –0,41°C. Wartość błędu RMSE, czyli przeciętne odchylenie wartości siatkowych od pomiarów stacyjnych, wynosiło około 1,4°C. Na tej podstawie uznano, że nie ma potrzeby stosowania korekty temperatur dla wszystkich szczytów i dane Open-Meteo można uznać za wystarczająco wiarygodne do celów projektu.

# Metody i narzędzia 

- **Python (pandas, requests, matplotlib)** – pobranie danych z API, przygotowanie miesięcznych agregacji, analiza i wizualizacja.
- **Analiza danych** – badanie sezonowości, porównania szczytów i regionów, rankingi oraz wskaźnik komfortu pogodowego.
- **Power BI i DAX** – interaktywny dashboard umożliwiający porównywanie szczytów i analizę sezonowych odchyleń.

# Wnioski z analizy

### 1. Wskaźnik komfortu pogodowego

Na potrzeby projektu opracowano autorski wskaźnik komfortu pogodowego, pozwalający porównać warunki na poszczególnych szczytach Korony Gór Polski.
Został on zbudowany w oparciu o cztery elementy:
- temperaturę (najwyższy komfort przy umiarkowanych wartościach, 10–20°C),
- opady (im niższe, tym wyższy komfort),
- prędkość wiatru (najwyższy komfort przy niskich wartościach),
- zachmurzenie (za najbardziej korzystne uznano umiarkowane zachmurzenie).

Wszystkie zmienne przeskalowano do wspólnego zakresu 0–100, a następnie połączono z równymi wagami. Uzyskano w ten sposób wskaźnik umożliwiający porównanie komfortu pogodowego pomiędzy szczytami i miesiącami.

![Heatmapa komfortu](plots/comfort/heatmap_all_peaks_colored.png)  

- Najbardziej komfortowe warunki w latach 2020–2024 występowały na szczytach niskich i średnich – najwyższe średnie wartości wskaźnika osiągnęły Chełmiec, Kłodzka Góra, Czupel, Biskupia Kopa i Turbacz.
- Szczyty wysokie (Rysy, Śnieżka, Babia Góra) uzyskały wyraźnie niższe wartości wskaźnika.
- Najkorzystniejszym miesiącem według przyjętego wskaźnika był lipiec. Dobre wyniki osiągały również czerwiec i sierpień, natomiast najniższe wartości przypadały na okres zimowy, szczególnie luty.

---

### 2. Porównanie regionów i grup wysokościowych
![Porównanie regionów i wysokości](plots/regions%20and%20heights/regions_heights_comparison.png)  
  
- Wysokość szczytu ma wyraźny związek z warunkami pogodowymi – wyżej położone szczyty charakteryzowały się niższymi temperaturami i na ogół większymi sumami opadów.
- Największe różnice między regionami dotyczyły poziomu temperatur. Najchłodniejsze były Tatry, natomiast najwyższe średnie temperatury występowały w Górach Świętokrzyskich i Pieninach. Pomimo tych różnic roczny przebieg temperatury był podobny we wszystkich regionach.
- Opady wykazywały wyraźną sezonowość – najwyższe miesięczne sumy przypadały zazwyczaj na okres od czerwca do sierpnia, a najniższe na marzec i kwiecień. Tatry wyróżniały się większymi opadami niż pozostałe analizowane regiony.

---

### 3. Roczny cykl pogodowy na przykładzie Rysów
![Sezonowość Rysy](plots/peaks/Rysy_all.png)  

- Temperatura: najniższe średnie wartości występowały w styczniu i lutym (od –10 do –12°C), a najwyższe w lipcu (około 7°C).
- Opady: największe miesięczne sumy przypadały na okres letni, przekraczając 140 mm, natomiast najmniejsze występowały w marcu i kwietniu.
- Śnieg: najwyższe średnie miesięczne opady odnotowano w styczniu (59 cm) i lutym (71 cm). W lipcu i sierpniu opady śniegu nie występowały.
- Wiatr: średnia z dobowych maksymalnych prędkości wiatru utrzymywała się na poziomie około 10–14 km/h, z nieco wyższymi wartościami zimą.
- Zachmurzenie: najwyższe występowało zimą (80–85%), a najniższe latem (około 60%).
- Nasłonecznienie: najwięcej godzin słonecznych przypadało na okres od maja do lipca, z maksimum w czerwcu (średnio 12,3 godziny dziennie).

Podsumowanie: Rysy charakteryzowały się najniższymi średnimi temperaturami spośród analizowanych szczytów oraz znacznymi opadami. Nawet w najcieplejszym miesiącu, lipcu, średnia temperatura wynosiła zaledwie około 7°C.

---

### 4. Ranking warunków pogodowych

Poniższe zestawienie przedstawia szczyty wyróżniające się pod względem poszczególnych parametrów pogodowych w latach 2020–2024.

| Kategoria                      | 1 miejsce        | 2 miejsce        | 3 miejsce        |
|--------------------------------|------------------|------------------|------------------|
| **Najbardziej deszczowe (mm)** | Tarnica (108.3)  | Rudawiec (107.7) | Śnieżnik (107.7) |
| **Najbardziej śnieżne (cm)**   | Rysy (24.7)      | Śnieżka (20.1)   | Tarnica (19.8)   |
| **Najbardziej wietrzne (km/h)** | Chełmiec (22.3)  | Waligóra (20.9)  | Ślęża (20.1)     |
| **Najbardziej słoneczne (h)**  | Rysy (28976.2)   | Radziejowa (27551.8) | Ślęża (27297.1) |
| **Najbardziej pochmurne (%)**  | Śnieżka (73.2)   | Rudawiec (72.0)  | Śnieżnik (72.0)  |
| **Najcieplejsze (°C)**         | Czupel (9.2)     | Kłodzka Góra (9.1) | Chełmiec (9.1)   |
| **Najzimniejsze (°C)**         | Rysy (–2.7)      | Śnieżka (1.6)    | Babia Góra (1.6) |

# Dashboard Power BI

Uzupełnieniem analizy jest dashboard Power BI. Umożliwia porównywanie warunków pogodowych na szczytach oraz analizę ich sezonowości w latach 2020–2024.

**[📊 Pobierz dashboard Power BI](dashboard/Dashboard%20-%20pogoda.pbix)**

1. Przegląd warunków pogodowych

![Przegląd warunków pogodowych KGP](dashboard/przeglad.png)

Pierwsza strona prezentuje ogólny obraz warunków na szczytach KGP:
- karty KPI ze średnią temperaturą, średnimi miesięcznymi opadami, średnim dziennym nasłonecznieniem i średnią z maksymalnych dobowych prędkości wiatru,
- roczny przebieg temperatury z pasmem średnich minimów i maksimów dobowych,
- mapę lokalizacji szczytów z rozróżnieniem grup wysokościowych,
- przełączany ranking TOP 7 dla opadów, nasłonecznienia i wiatru,
- wykres zależności między wysokością szczytu a temperaturą z linią trendu.

Raport umożliwia filtrowanie danych według zakresu lat, grupy wysokościowej i szczytu. 

2. Sezonowość warunków pogodowych

![Sezonowość warunków pogodowych KGP](dashboard/sezonowosc.png)

Druga strona pozwala analizować odchylenia średnich wartości miesięcznych od średniej dla danego szczytu. Obejmuje:
- przełącznik sześciu parametrów: temperatury, opadów, śniegu, wiatru, nasłonecznienia i zachmurzenia,
- karty wskazujące miesiące o najwyższych i najniższych średnich odchyleniach,
- wykres liniowy średnich odchyleń w kolejnych miesiącach,
- heatmapę do porównywania wzorców sezonowych pomiędzy wszystkimi 28 szczytami,
- tooltipy prezentujące wartości i punkt odniesienia dla obliczonych odchyleń.

Odchylenia służą tutaj do opisu sezonowości, a nie anomalii względem wieloletniej normy klimatycznej.
