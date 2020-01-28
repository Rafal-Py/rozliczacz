# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:30:15 2019

@author: Rafał
"""

def jaki_ostatni_dobowy(lok_bilety):
    """Funkcja ładuje bilety.txt i zwraca ostatni rozliczony raport dobowy"""
    try:
        with open(lok_bilety) as plik_bilety:
            list_bilety = list(plik_bilety)    
            ostatni_wiersz = list_bilety[-1].split()        
            ostatni = int(ostatni_wiersz[1])             
    except:
        ostatni = 0
    return ostatni   