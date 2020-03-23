# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:41:39 2019

@author: Rafał
"""
import os.path
from jaki_ostatni_dobowy import jaki_ostatni_dobowy
from przetwarzaj_raport import przetwarzaj_raport
from zapisz_bilety import zapisz_bilety
from jaki_raport import jaki_raport
from zapisz_do_pliku import zapisz_do_pliku
from wczytaj_bilety_dotk import wczytaj_dotk
from distutils import dir_util
import tkinter as tk

#Na czas testów te lokalizacje są wyłączone
#folder = r'\\192.168.1.3\@001 DZIAŁALNOŚĆ\001 ORGANIZACJA KONCERTÓW\01 ROZLICZENIA KONCERTÓW\02 ROZLICZENIA BILETÓW\BGH16010347'
#lok_bilety = r'\\192.168.1.3\@001 DZIAŁALNOŚĆ\001 ORGANIZACJA KONCERTÓW\01 ROZLICZENIA KONCERTÓW\02 ROZLICZENIA BILETÓW\bilety.txt'
folder_c = r'C:\Users\Public\Documents\Novitus\CDData\BGH16010347'

#Na czas testów, te lokalizacje są obowiązujące
folder = r'C:\Python\rozliczacz-git\BGH16010347'
lok_bilety = r'C:\Python\rozliczacz-git\bilety.txt'
#lok_raport = 'F:\\Bilety_program\\BAV11006958\\1100\\1162.txt'   

def rozliczacz(folder, lok_bilety, ostatni):        
    #Skopiuj dane kasy fiskalnej z pamięci lokalnej komputera 
    #na dysk sieciowy, na którym będą dokonywane dalsze operacje
    try:
        dir_util.copy_tree(str(folder_c), str(folder))
    except:
        pass
    
    #lok_raport = 'C:\\Bilety\\BAV11006958\\1100\\' + str(ostatni+1) + '.txt'
    #label['text'] = 'Ostatni raport dobowy: ' + str(ostatni) + '\n'
    
    text_wynik = []
    while True:
        lok_raport = jaki_raport(ostatni, folder)    
        #lok_raport = 'C:\\Bilety\\BAV11006958\\1100\\1172.txt'    
        if not os.path.isfile(lok_raport):        
            break
        else:
            raport_dobowy = {}        
            raport_dobowy['numer raportu'] = ostatni+1
            przetwarzaj_raport(ostatni, raport_dobowy, lok_raport)
            string = zapisz_bilety(raport_dobowy)
            zapisz_do_pliku(string, lok_bilety)
            text_wynik.append(string.strip())
            ostatni = jaki_ostatni_dobowy(lok_bilety)       
    for i in text_wynik:
        list_box.insert(tk.END, i)
    #label['text'] += text_wynik    
    
HEIGHT = 600
WIDTH = 900

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor = 'n')

upper_label = tk.Label(frame, text = "..."+folder[-60::], font = ('Gill Sans MT', 9))
upper_label.place(relwidth=0.65, relheight=1)

#entry = tk.Entry(frame, font = 40)
#entry.place(relwidth=0.65, relheight=1)

#Jaki jest ostatni rozliczony raport dobowy?
ostatni = jaki_ostatni_dobowy(lok_bilety)

button = tk.Button(frame, text="Rozlicz raporty", font = ('Gill Sans MT', 18), command = lambda: rozliczacz(folder, lok_bilety, ostatni))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#label = tk.Label(lower_frame, font = ('Gill Sans MT', 16), anchor='nw', justify='left', bd=4)
#label.place(relwidth=1, relheight=1)

list_box = tk.Listbox(lower_frame, font = ('Gill Sans MT', 16))
scroll = tk.Scrollbar(lower_frame, command = list_box.yview)
list_box.config(yscrollcommand = scroll.set)
list_box.pack(side = 'left', fill = 'both', expand = 1)
scroll.pack(side = 'right', fill = 'y')

list_box.insert(tk.END,'Ostatni raport dobowy: ' + str(ostatni))
list_box.insert(tk.END,'Data               Nr       VAT')
for line in wczytaj_dotk(lok_bilety):
    list_box.insert(tk.END, line)

root.mainloop()