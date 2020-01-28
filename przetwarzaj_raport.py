# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:29:29 2019

@author: Rafał
"""
import re

def przetwarzaj_raport(ostatni, slownik, lok_raport):
    """Funkcja edytuje słownik wypełniony biletami z raportu dobowego"""
    
    def usun_niepotrzebne(raport):
    
        def usun_anulowany(pattern, matches, raport):
            try:
                match = next(matches)            
                raport = raport[ : match.start()-418] + raport[match.end()+322 : ]            
                matches = pattern.finditer(raport)            
                raport = usun_anulowany(pattern, matches, raport)
            except:            
                return raport
            return raport
    
        pattern = re.compile(r'(NIEFISKALNY)(.|\n)*(NIEFISKALNY)')            
        matches = pattern.finditer(raport)
        try:
            match = next(matches)        
            raport = raport[ : match.start()-377] + raport[match.end()+223 : ]
        except:
            pass        
        
        pattern = re.compile(r'(P A R A G O N   F I S K A L N Y)((?:.|\n){200,364})(PARAGON ANULOWANY)')    
        matches = pattern.finditer(raport) 
        raport = usun_anulowany(pattern, matches, raport)    
        return raport
    
    def czytaj_bilety_wiersza(wiersz):
        """Funkcja przetwarza wiersz i zwraca ilosc_biletu, wartosc_biletu"""
        poz_gw = wiersz.find('*')
        poz_kr = wiersz.find('.')
        poz_u = wiersz.find('u')
        wartosc_biletu = int(wiersz[poz_gw + 1 : poz_kr])    
        ilosc_biletu = int(wiersz[poz_u + 1 : poz_gw])
        #prawidłowo działa
        return (ilosc_biletu, wartosc_biletu)

    def laduj_bilety(slownik, b5, b10, b15, b20, b25, b30, b35, b40, b50, b70):
        """Funkcja ładuje znalezione bilety do słownika"""
        if b5 != 0:
            slownik[5] = b5
        if b10 != 0:
            slownik[10] = b10
        if b15 != 0:
            slownik[15] = b15
        if b20 != 0:
            slownik[20] = b20
        if b25 != 0:
            slownik[25] = b25
        if b30 != 0:
            slownik[30] = b30
        if b35 != 0:
            slownik[35] = b35
        if b40 != 0:
            slownik[40] = b40
        if b50 != 0:
            slownik[50] = b50
        if b70 != 0:
            slownik[70] = b70    
    
    b5, b10, b15, b20, b25, b30, b35, b40, b50, b70 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    with open(lok_raport) as raport:        
        ok_raport = raport.read()
    
    ok_raport = usun_niepotrzebne(ok_raport).split('\n')
    
    i=0
    while i < len(ok_raport):
        wiersz = ok_raport[i]
                    
        if wiersz.startswith(' Plik utworzono:'):            
            slownik['data raportu'] = wiersz.split()[2]            
        elif wiersz.startswith(' Bilet'):
            dane = czytaj_bilety_wiersza(wiersz)            
            if dane[1] == 5:
                b5 += dane[0]                        
            elif dane[1] == 10:
                b10 += dane[0]
            elif dane[1] == 15:
                b15 += dane[0]
            elif dane[1] == 20:
                b20 += dane[0]
            elif dane[1] == 25:
                b25 += dane[0]
            elif dane[1] == 30:
                b30 += dane[0]                        
            elif dane[1] == 35:
                b35 += dane[0]
            elif dane[1] == 40:
                b40 += dane[0]                        
            elif dane[1] == 50:
                b50 += dane[0]                        
            elif dane[1] == 70:
                b70 += dane[0]                            
        elif wiersz.startswith(' Kwota PTU B'):                
            slownik['vat'] = wiersz.split()[3]                
            break            
        i += 1
    laduj_bilety(slownik, b5, b10, b15, b20, b25, b30, b35, b40, b50, b70) 