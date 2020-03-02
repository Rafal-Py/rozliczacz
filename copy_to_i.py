#! python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:35:48 2020

@author: Rafał

Skrypt kopiuje dane kasy fiskalnej z pamięci lokalnej komputera 
na dysk sieciowy, na którym będą dokonywane dalsze operacje
"""

from distutils import dir_util
from pathlib import Path

folder_c = Path(r'C:\Users\Public\Documents\Novitus\CDData\BGH16010347')

def copy_to_i(folder_c, folder):
    dir_util.copy_tree(str(folder_c), str(folder))    

if __name__ == "__main__":
    folder = Path(r'I:\@001 DZIAŁALNOŚĆ\001 ORGANIZACJA KONCERTÓW\01 ROZLICZENIA KONCERTÓW\02 ROZLICZENIA BILETÓW\BGH16010347')
    #folder = Path(r'C:\Python\BGH16010347')
    copy_to_i(folder_c, folder)