#!/usr/bin/env python
# coding: utf-8

"""
Created on Sat Nov 11 13:37:34 2023

@author: nopa1001
"""
# In[1]:
import csv
sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'


with open(sciezka_do_pliku, 'r') as plik_csv:
    czytnik = csv.reader(plik_csv)

    for wiersz in czytnik:
        print(wiersz)
# In[2]:
import csv

def wczytaj_dane_csv(sciezka_do_pliku):
    with open(sciezka_do_pliku, 'r', newline='', encoding='utf-8') as plik_csv:
        czytnik = csv.DictReader(plik_csv)
        dane_zakupowe = list(czytnik)
    return dane_zakupowe

def wydatki_na_sezony(dane_zakupowe):
    if 'Season' not in dane_zakupowe[0]:
        print("Brak informacji o sezonie ")
        return None

    if 'Purchase Amount (USD)' not in dane_zakupowe[0]:
        print("Brak informacji o kwocie zakupu ")
        return None

    wydatki_sezonowe = {'Spring': 0, 'Summer': 0, 'Fall': 0, 'Winter': 0}

    for zakup in dane_zakupowe:
        sezon = zakup['Season']

        if sezon not in wydatki_sezonowe:
            print(f"Nieznany sezon: {sezon}")
            continue

        kwota_zakupu = float(zakup['Purchase Amount (USD)'])

        wydatki_sezonowe[sezon] += kwota_zakupu

    return wydatki_sezonowe

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = wczytaj_dane_csv(sciezka_do_pliku)

wynik = wydatki_na_sezony(dane_zakupowe)
print(wynik)
# In[3]:
from collections import Counter

def najczestsze_kolory_torebek(dane_zakupowe):
    if 'Item Purchased' not in dane_zakupowe[0] or 'Color' not in dane_zakupowe[0]:
        print("Brak informacji o zakupach lub kolorach w danych zakupowych.")
        return None

    torebki = [zakup for zakup in dane_zakupowe if zakup['Item Purchased'] == 'Handbag']

    kolory_torebek = [torebka['Color'] for torebka in torebki]

    licznik_kolorow = Counter(kolory_torebek)

    najczestsze_kolory = licznik_kolorow.most_common(3)
    
    return najczestsze_kolory

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = wczytaj_dane_csv(sciezka_do_pliku)

wynik = najczestsze_kolory_torebek(dane_zakupowe)
print(wynik)
# In[4]:
def mezczyzni_18_25_lat_bluzki_XL(dane_zakupowe):
    wynik = []

    for zakup in dane_zakupowe:
        #warunki: mężczyzna, wiek 18-25 lat, bluzki w rozmiarze XL
        if (
            zakup.get('Gender') == 'Male' and
            18 <= int(zakup.get('Age', 0)) <= 25 and
            zakup.get('Item Purchased') == 'Blouse' and
            zakup.get('Size') == 'XL'
        ):
            wynik.append(zakup)

    return wynik

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = wczytaj_dane_csv(sciezka_do_pliku)

wynik = mezczyzni_18_25_lat_bluzki_XL(dane_zakupowe)
print(wynik)
# In[5]:
import matplotlib.pyplot as plt

def wykres_rozkladu_ubran_kobiet_25_45(dane_zakupowe):
    #kobiety w wieku 25-45 lat
    kobiety_25_45 = [zakup for zakup in dane_zakupowe if
                     zakup.get('Gender') == 'Female' and
                     25 <= int(zakup.get('Age', 0)) <= 45]
    
    rodzaje_ubran = {}
    for zakup in kobiety_25_45:
        rodzaj_ubrania = zakup.get('Item Purchased', 'Nieokreślony')
        rodzaje_ubran[rodzaj_ubrania] = rodzaje_ubran.get(rodzaj_ubrania, 0) + 1

    plt.figure(figsize=(8, 8))
    plt.pie(rodzaje_ubran.values(), labels=rodzaje_ubran.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Rozkład rodzajów kupowanych ubrań wśród kobiet (25-45 lat)')
    plt.show()

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = wczytaj_dane_csv(sciezka_do_pliku)

wykres_rozkladu_ubran_kobiet_25_45(dane_zakupowe)
# In[6]:
import matplotlib.pyplot as plt

def histogram_rozkladu_wieku(dane_zakupowe):
    wieki = [int(zakup.get('Age', 0)) for zakup in dane_zakupowe]

    plt.figure(figsize=(10, 6))
    plt.hist(wieki, bins=range(min(wieki), max(wieki) + 5, 5), color='skyblue', edgecolor='black')
    plt.xlabel('Wiek')
    plt.ylabel('Liczba osób')
    plt.title('Rozkład wieku w danych zakupowych')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = wczytaj_dane_csv(sciezka_do_pliku)

histogram_rozkladu_wieku(dane_zakupowe)
# In[7]:
import pandas as pd

def wydatki_na_produkty(dane_zakupowe):
    df = pd.DataFrame(dane_zakupowe)

    if 'Purchase Amount (USD)' not in df.columns:
        print("Brak informacji o kwocie zakupu w danych zakupowych.")
        return None

    df['Purchase Amount (USD)'] = pd.to_numeric(df['Purchase Amount (USD)'], errors='coerce')

    wydatki_na_produkty = df.groupby('Category')['Purchase Amount (USD)'].sum()

    return wydatki_na_produkty.to_dict()

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = pd.read_csv(sciezka_do_pliku)

wynik = wydatki_na_produkty(dane_zakupowe)
print(wynik)
# In[8]:
import pandas as pd

def top5_miast_na_sukienki(dane_zakupowe):
    df = pd.DataFrame(dane_zakupowe)

    if 'Item Purchased' not in df.columns or 'Location' not in df.columns:
        print("Brak informacji o zakupach lub miastach")
        return None

    sukienki = df[df['Item Purchased'] == 'Dress']

    liczba_sukienek_w_miastach = sukienki.groupby('Location').size()

    top5_miast = liczba_sukienek_w_miastach.nlargest(5)

    return top5_miast.to_dict()

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = pd.read_csv(sciezka_do_pliku)

wynik = top5_miast_na_sukienki(dane_zakupowe)
print(wynik)
# In[9]:
import pandas as pd

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = pd.read_csv(sciezka_do_pliku)


def kobiety_subskrybentki_powyzej_15_zakupow(dane_zakupowe):
    df = pd.DataFrame(dane_zakupowe)

    wymagane_kolumny = ['Gender', 'Age', 'Subscription Status', 'Previous Purchases']
    if not set(wymagane_kolumny).issubset(df.columns):
        print("Brak wymaganych informacji")
        return None

    kobiety_subskrybentki = df[
        (df['Gender'] == 'Female') &
        (df['Age'].astype(float) < 40) &
        (df['Subscription Status'] == 'Yes') &
        (df['Previous Purchases'].astype(float) > 15)
    ]

    return kobiety_subskrybentki

wynik = kobiety_subskrybentki_powyzej_15_zakupow(dane_zakupowe)
print(wynik)
# In[10]:
import pandas as pd
import matplotlib.pyplot as plt

def wykres_rozkladu_metod_platnosci_wiek(dane_zakupowe):
    df = pd.DataFrame(dane_zakupowe)

    if 'Age' not in df.columns or 'Payment Method' not in df.columns:
        print("Brak informacji o wieku lub metodach płatności")
        return None

    df = df.dropna(subset=['Age', 'Payment Method'])

    plt.figure(figsize=(12, 6))
    plt.scatter(df['Age'], df['Payment Method'], alpha=0.5)
    plt.xlabel('Wiek')
    plt.ylabel('Metoda Płatności')
    plt.title('Rozkład Metod Płatności w Zależności od Wieku')
    plt.show()

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = pd.read_csv(sciezka_do_pliku)

wykres_rozkladu_metod_platnosci_wiek(dane_zakupowe)
# In[11]:
import pandas as pd
import matplotlib.pyplot as plt

def histogram_rozkladu_dostawy_wg_plci(dane_zakupowe):
    df = pd.DataFrame(dane_zakupowe)

    if 'Gender' not in df.columns or 'Shipping Type' not in df.columns:
        print("Brak informacji o płci lub rodzaju dostawy ")
        return None

    df = df.dropna(subset=['Gender', 'Shipping Type'])

    kobiety = df[df['Gender'] == 'Female']
    mezczyzni = df[df['Gender'] == 'Male']

    # Tworzy histogramy
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(kobiety['Shipping Type'], bins='auto', color='skyblue', edgecolor='black')
    plt.xlabel('Rodzaj Dostawy')
    plt.ylabel('Liczba Transakcji')
    plt.title('Rozkład Rodzaju Dostawy - Kobiety')

    plt.subplot(1, 2, 2)
    plt.hist(mezczyzni['Shipping Type'], bins='auto', color='lightcoral', edgecolor='black')
    plt.xlabel('Rodzaj Dostawy')
    plt.ylabel('Liczba Transakcji')
    plt.title('Rozkład Rodzaju Dostawy - Mężczyźni')

    plt.tight_layout()
    plt.show()

sciezka_do_pliku = 'C:/Users/nopa1001/Downloads/shopping_behavior_updated.csv'

dane_zakupowe = pd.read_csv(sciezka_do_pliku)

histogram_rozkladu_dostawy_wg_plci(dane_zakupowe)
