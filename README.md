# Analiza warunków pogodowych Korony Gór Polski (2020–2024)

# Opis projektu

Projekt analizuje warunki pogodowe na 28 szczytach Korony Gór Polski (KGP) w latach 2020–2024. Uwzględnia sezonowość temperatur, opadów, wiatru, zachmurzenia i nasłonecznienia. Analiza pozwala porównać szczyty między sobą, a także w ramach regionów oraz grup wysokościowych. Celem projektu było wskazanie szczytów o najbardziej ekstremalnych warunkach oraz określenie miesięcy sprzyjających górskim wędrówkom.

# Cele analizy

1.	Określenie najbardziej deszczowych miesięcy dla każdego szczytu.
2.	Analiza sezonowości temperatur, opadów i wiatru.
3.	Porównanie różnic klimatycznych pomiędzy regionami (Tatry, Sudety, Beskidy, Góry Świętokrzyskie, Pieniny).
4.	Porównanie warunków pogodowych pomiędzy grupami wysokościowymi (<1000 m, 1000–1500 m, >1500 m).
5.	Wskazanie szczytów najbardziej ekstremalnych pod względem klimatycznym.
6.	Wyciągnięcie praktycznych wniosków przydatnych przy planowaniu wycieczek.

# Dane

•	Źródło: Open-Meteo API
•	Okres analizy: 2020–2024
•	Agregacja: dane dzienne przekształcone do wartości miesięcznych
•	Zmienne: średnia, maksymalna i minimalna temperatura, suma opadów deszczu i śniegu, prędkość wiatru, zachmurzenie

Dane Open-Meteo mają charakter siatkowy, co oznacza, że wartości pogodowe są wyznaczane na podstawie interpolacji z modeli numerycznych w regularnych punktach siatki, a nie pochodzą bezpośrednio ze stacji pomiarowych, co może wpływać na ich dokładność.
Dla Śnieżki, jedynego szczytu KGP na którym znajduje się obserwatorium meteorologiczne, przeprowadzono porównanie danych siatkowych Open-Meteo z danymi stacyjnymi IMGW. W badanym okresie średnia różnica wyniosła –0,41°C. Wartość błędu RMSE, czyli przeciętne odchylenie wartości siatkowych od pomiarów stacyjnych, wynosiło około 1,4°C. Na tej podstawie uznano, że nie ma potrzeby stosowania korekty temperatur dla wszystkich szczytów i dane Open-Meteo można uznać za wystarczająco wiarygodne do celów projektu.

# Metody

•	Opracowanie profilu klimatycznego każdego szczytu
•	Wykresy sezonowości temperatur, opadów i wiatru
•	Analizy porównawcze regionów i grup wysokościowych
•	Rankingi szczytów pod kątem ekstremalnych warunków pogodowych
•	Heatmapa wskaźnika komfortu

# Rezultaty
•	Profil klimatyczny każdego z 28 szczytów
•	Porównania między regionami i grupami wysokościowymi
•	Rankingi najbardziej deszczowych, wietrznych i zimnych szczytów
•	Wyliczenie wskaźnika komfortu i identyfikacja najbardziej sprzyjających szczytów
•	Zbiór wykresów prezentujących warunki pogodowe

# Wnioski z analizy

Analiza pozwoliła:
- opracować profil klimatyczny każdego z 28 szczytów,
- porównać regiony i grupy wysokościowe,
- przygotować rankingi najbardziej deszczowych, wietrznych i zimnych szczytów,
- obliczyć wskaźnik komfortu i wskazać najbardziej sprzyjające szczyty,
- stworzyć zestaw wizualizacji prezentujących warunki pogodowe.

Najważniejsze obserwacje to:

### 1. Heatmapa wskaźnika komfortu

**Wskaźnik komfortu** został zbudowany w oparciu o cztery elementy:
- średnia temperatura (im bliżej umiarkowanych wartości, tym wyższy komfort),
- suma opadów (niższe opady = wyższy komfort),
- prędkość wiatru (niższe wartości = wyższy komfort),
- zachmurzenie (średnie wartości uznane za najbardziej korzystne).

Wszystkie zmienne zostały znormalizowane i przeskalowane do wspólnej skali (0–100), a następnie zsumowane z równymi wagami, tworząc syntetyczny wskaźnik komfortu dla każdego szczytu i miesiąca.

![Heatmapa komfortu](plots/comfort_heatmap.png)  

- Najbardziej komfortowe warunki występują na szczytach średnich wysokości (np. Orlica, Mogielica, Turbacz).  
- Szczyty wysokie (Rysy, Śnieżka, Babia Góra) mają wyraźnie niższy wskaźnik komfortu zimą, co potwierdza ich bardziej ekstremalne warunki.  
- Najkorzystniejsze miesiące dla większości szczytów to lipiec i sierpień.  

---

### 2. Porównanie regionów i grup wysokościowych
![Porównanie regionów i wysokości](plots/regions_groups_comparison.png)  

- Tatry są najzimniejsze i najbardziej śnieżne spośród analizowanych regionów.  
- Sudety wyróżniają się największą wietrznością oraz dużą zmiennością opadów.  
- Beskidy i Góry Świętokrzyskie mają bardziej umiarkowany i przewidywalny klimat.  
- Analiza grup wysokościowych potwierdza: szczyty wysokie są zimniejsze i bardziej wilgotne, natomiast średnie wysokości mają najbardziej sprzyjające warunki turystyczne.  

---

### 3. Roczny cykl pogodowy – przykład: Rysy
![Sezonowość Rysy](plots/rysy_cycle.png)  

- Rysy pokazują wyraźny kontrast sezonowy: długa i mroźna zima (październik–maj) oraz krótki, ale stabilny sezon letni.  
- Zimą dominują intensywne opady śniegu, niskie temperatury i wysokie zachmurzenie.  
- Latem występuje więcej słońca, wyższe temperatury i względnie mniejsze opady śniegu, co czyni lipiec i sierpień najlepszym okresem na wycieczki w Tatry.  

---

### 4. Podsumowanie ogólne
- **Tatry** → najzimniejsze i najbardziej śnieżne.  
- **Sudety** → najbardziej wietrzne.  
- **Średnie szczyty (1000–1500 m)** → najbardziej komfortowe warunki dla turystów.  
- **Najlepsze miesiące** na górskie wędrówki to lipiec i sierpień.  
