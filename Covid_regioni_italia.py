#!/usr/bin/env python
# coding: utf-8
import reg_def

reg = str(input("\nInserire il nome della reg_def.regione per vedere le statistiche: "))

if reg == "Abruzzo":
    reg_def.regione(reg,0,1313000)
    
elif reg == "Basilicata":
    reg_def.regione(reg,1,567118)

elif reg == "Bolzano":
    reg_def.regione(reg,2,106951)
    
elif reg == "Calabria":
    reg_def.regione(reg,3,1957000)
    
elif reg == 'Campania':
    reg_def.regione(reg,4,1957000)

elif reg == 'Emilia Romagna':
    reg_def.regione(reg,5,4453000)

elif reg == "Friuli Venezia Giulia":
    reg_def.regione(reg,6,1216000)

elif reg == "Lazio":
    reg_def.regione(reg,7,5897000)

elif reg == "Liguria":
    reg_def.regione(reg,8,1557000)

elif reg == "Lombardia":
    reg_def.regione(reg,9,10040000)

elif reg == "Marche":
    reg_def.regione(reg,10,1532000)

elif reg == "Molise":
    reg_def.regione(reg,11,308493)

elif reg == "Piemonte":
    reg_def.regione(reg,12,4376000)

elif reg == "Puglia":
    reg_def.regione(reg,13,4048000)

elif reg == "Sardegna":
    reg_def.regione(reg,14,1648000)

elif reg == "Sicilia":
    reg_def.regione(reg,15,5027000)

elif reg == "Toscana":
    reg_def.regione(reg,16,3737000)

elif reg == "Trento":
    reg_def.regione(reg,17,118288)

elif reg == "Umbria":
    reg_def.regione(reg,18,884640)

elif reg == "Aosta":
    reg_def.regione(reg,19,126202)

elif reg == "Veneto":
    reg_def.regione(reg,20,4905000)
    
else:
    print('\nLa reg_def.regione inserita non esiste..\n')

import os
import sys

restart = input("\nVuoi riprovare?: ")

if restart == "s":
    os.execl(sys.executable, sys.executable, * sys.argv) 
else:
    print("\nIl programma esce..")
    sys.exit(0)