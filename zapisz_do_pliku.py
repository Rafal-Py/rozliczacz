# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:41:46 2020

@author: Rafał
"""

def zapisz_do_pliku(string, lok_bilety):    
    with open(lok_bilety, 'a') as bilety:
        bilety.write(string)
        