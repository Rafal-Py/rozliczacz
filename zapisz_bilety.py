# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:30:51 2019

@author: Rafał
"""

def zapisz_bilety(slownik):
    string = slownik.get('data raportu','brak daty') + '     ' + str(slownik['numer raportu']) + '     ' + str(slownik['vat']) + '     '
    if 5 in slownik:
        string += str(slownik[5]) + '* 5     '
    if 10 in slownik:
        string += str(slownik[10]) + '*10     '
    if 15 in slownik:
        string += str(slownik[15]) + '*15     '
    if 20 in slownik:
        string += str(slownik[20]) + '*20     '
    if 25 in slownik:
        string += str(slownik[25]) + '*25     '
    if 30 in slownik:
        string += str(slownik[30]) + '*30     '
    if 35 in slownik:
        string += str(slownik[35]) + '*35     '
    if 40 in slownik:
        string += str(slownik[40]) + '*40     '
    if 50 in slownik:
        string += str(slownik[50]) + '*50     '
    if 70 in slownik:
        string += str(slownik[70]) + '*70     '
    string += '\n'
    return string
    
   