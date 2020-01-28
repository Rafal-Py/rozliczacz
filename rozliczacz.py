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
import tkinter as tk

folder = r'I:\@001 DZIAŁALNOŚĆ\001 ORGANIZACJA KONCERTÓW\01 ROZLICZENIA KONCERTÓW\02 ROZLICZENIA BILETÓW\BGH16010347'
lok_bilety = r'I:\@001 DZIAŁALNOŚĆ\001 ORGANIZACJA KONCERTÓW\01 ROZLICZENIA KONCERTÓW\02 ROZLICZENIA BILETÓW\bilety.txt'

def rozliczacz(folder, lok_bilety):    
    #folder = 'I:\\@001 DZIAŁALNOŚĆ\\001 ORGANIZACJA KONCERTÓW\\01 ROZLICZENIA KONCERTÓW\\02 ROZLICZENIA BILETÓW\\BAV11006958'
    #lok_bilety = 'I:\\@001 DZIAŁALNOŚĆ\\001 ORGANIZACJA KONCERTÓW\\01 ROZLICZENIA KONCERTÓW\\02 ROZLICZENIA BILETÓW\\bilety.txt'
    #lok_raport = 'F:\\Bilety_program\\BAV11006958\\1100\\1162.txt'                
    ostatni = jaki_ostatni_dobowy(lok_bilety)
    #lok_raport = 'C:\\Bilety\\BAV11006958\\1100\\' + str(ostatni+1) + '.txt'
    #label['text'] = 'Ostatni raport dobowy: ' + str(ostatni) + '\n'
    list_box.insert(tk.END,'Ostatni raport dobowy: ' + str(ostatni))
    list_box.insert(tk.END,'Data               Nr       VAT')    
    text_wynik = []
    while True:
        lok_raport = jaki_raport(ostatni, folder)    
        #lok_raport = 'C:\\Bilety\\BAV11006958\\1100\\1172.txt'    
        if not os.path.isfile(lok_raport):        
            break
        else:
            slownik = {}        
            slownik['numer raportu'] = ostatni+1
            przetwarzaj_raport(ostatni, slownik, lok_raport)
            string = zapisz_bilety(slownik)
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

button = tk.Button(frame, text="Rozlicz raporty", font = ('Gill Sans MT', 18), command = lambda: rozliczacz(folder, lok_bilety))
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

root.mainloop()



#rozliczacz()