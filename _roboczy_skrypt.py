# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:30:04 2020

@author: Rafał
"""
import re

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
    for match in matches:
        if match:
            raport = raport[ : match.start()-377] + raport[match.end()+223 : ]
    
    pattern = re.compile(r'(P A R A G O N   F I S K A L N Y)((?:.|\n){200,364})(PARAGON ANULOWANY)')    
    matches = pattern.finditer(raport)
#    for match in matches:
#        print(match.group(2))
    raport = usun_anulowany(pattern, matches, raport)    
    return raport
#    return raport[ : match.start()-418] + raport[match.end()+322 : ]
    
lok_raport = r"H:\2020 Bilety\BGH16010347\0001\0007.txt"

with open(lok_raport) as raport:
    ok_raport = raport.read()

#print(usun_niepotrzebne(ok_raport))
#usun_niepotrzebne(ok_raport)
