# Analiza korpusu językowego i aplikacja do nauki języka

Projekt służy do podstawowej analizy korpusu tekstowego wybranego języka oraz oferuje prostą aplikację webową do nauki budowy zdań w języku angielskim.  
Obejmuje:

- analizę częstotliwości słów,
- wizualizację prawa Zipfa,
- budowę grafu współwystępowania słów (bigramy),
- ekstrakcję najczęstszych rzeczowników przy użyciu NLP,
- interaktywną aplikację do generowania zdań w czasach prostych (Present / Past / Future Simple).

Projekt był tworzony na potrzeby zajęć akademickich.


## Struktura repozytorium

```
app_learning/    # Aplikacja webowa do nauki języka
corpus/          # Folder z korpusami tekstowymi (txt)
results/         # Folder z wynikami analizy
scripts/         # Skrypty analityczne
  core.py        # Analiza bigramów i graf współwystępowania słów
  frequency.py   # Analiza częstotliwości słów i prawo Zipfa
  top_nouns.py   # Ekstrakcja najczęstszych rzeczowników przy użyciu NLP
```

## App Learning – interaktywna aplikacja do nauki języka

Folder `app_learning/` zawiera prostą aplikację webową typu **Sentence Builder**, która umożliwia generowanie zdań w języku angielskim i ich tłumaczeń na język polski.

**Funkcjonalności:**

- Budowanie zdań w czasach prostych: Present / Past / Future Simple
- Obsługa typów zdań: Affirmative / Negative / Question
- Wybór podmiotu, czasownika, rzeczownika, liczby i opcjonalnie przymiotnika
- Losowanie zdań
- Automatyczne generowanie tłumaczenia na język polski

**Pliki:**

* `index.html` – interfejs aplikacji
* `style.css` – style strony
* `nouns.json` / `verbs.json` – baza danych słów

**Uruchomienie lokalne:**

1. Otwórz `app_learning/index.html` w przeglądarce.
2. Aplikacja załaduje dane z `nouns.json` i `verbs.json`.
3. Wybierz parametry zdania i kliknij **GENERUJ ZDANIE** lub **Losuj**.


## Dane wejściowe

W folderze `corpus/` należy umieścić plik tekstowy z korpusem w formacie:

```
<nazwa_języka>.txt
```

Domyślnym językiem jest **litewski**.


## Opis skryptów

### 1. `frequency.py` – analiza częstotliwości i prawo Zipfa

**Funkcje:**
- czyści tekst,
- liczy częstotliwości słów,
- zapisuje listę do pliku CSV,
- tworzy wykres prawa Zipfa,
- oblicza, ile słów wystarcza do zrozumienia 90% tekstu.

**Uruchomienie:**
```bash
python scripts/frequency.py litewski
```

**Wyniki:**
- `results/freq_list.csv` – lista słów i ich częstotliwości,
- `results/ZipfLaw.png` – wykres prawa Zipfa,
- komunikat w terminalu z liczbą słów potrzebnych do zrozumienia 90% tekstu.

### 2. `core.py` – graf współwystępowania słów (bigramy)

**Funkcje:**
- dzieli tekst na zdania i słowa,
- tworzy bigramy (pary kolejnych słów),
- liczy częstość występowania bigramów,
- tworzy graf słów z wagami odpowiadającymi częstotliwości bigramów,
- zapisuje wizualizację grafu do pliku PNG.

**Uruchomienie:**
```bash
python scripts/core.py litewski
```

**Wyniki:**
- `results/language_core.png` – graf współwystępowania słów,
- lista 50 najczęstszych bigramów w terminalu.

### 3. `top_nouns.py` – ekstrakcja najczęstszych rzeczowników

**Funkcje:**
- ładuje listę najczęstszych słów z `freq_list.csv`,
- analizuje 2000 najczęstszych słów przy użyciu modelu NLP stanza,
- wyodrębnia rzeczowniki,
- zapisuje 55 najczęstszych rzeczowników do pliku TXT.

**Uruchomienie:**
```bash
python scripts/top_nouns.py lt
```

**Wyniki:**
- `results/top_nouns.txt` – lista najczęstszych rzeczowników.


## Wymagania

- Python 3.8+
- Pakiety Python:
  ```bash
  pip install -r requirements.txt
  ```

- Przeglądarka internetowa (do `app_learning`)

- Po pierwszym uruchomieniu `top_nouns.py` model językowy zostanie automatycznie pobrany.


## 🔹 Przykładowy przepływ pracy

1. Umieść plik korpusu w folderze `corpus/`.
2. Wygeneruj listę częstotliwości i wykres Zipfa:
   ```bash
   python scripts/frequency.py litewski
   ```
3. Utwórz graf bigramów:
   ```bash
   python scripts/core.py litewski
   ```
4. Wyodrębnij najczęstsze rzeczowniki:
   ```bash
   python scripts/top_nouns.py lt
   ```

## 🔹 Uwagi

- Wszystkie wyniki są zapisywane w folderze `results/`.
- Skrypty automatycznie tworzą folder `results/`, jeśli nie istnieje.
- Domyślnym językiem jest litewski, ale można analizować inne języki obsługiwane przez stanza.
