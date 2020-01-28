# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 16:31:19 2019

@author: Rafał
"""

def jaki_raport(ostatni, folder):
    if ostatni < 9:        
        return folder + '\\0001\\000'+ str(ostatni+1) + '.txt'
    elif ostatni < 99:        
        return folder + '\\0001\\00'+ str(ostatni+1) + '.txt'
    elif ostatni < 999:        
        return folder + '\\0' + str((ostatni+1) // 100) + '00\\0' + str(ostatni+1) + '.txt'    
    else:        
        return folder + '\\' + str((ostatni+1) // 100) + '00\\' + str(ostatni+1) + '.txt'