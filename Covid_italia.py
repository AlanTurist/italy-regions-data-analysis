#!/usr/bin/env python
# coding: utf-8

# ## Script takes data from GitHup repository .csv

import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")
import pandas as pd
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-latest.csv'
df = pd.read_csv(url,index_col=0, sep=",")

# ## Analyse data taken from .csv

D1 = df['ricoverati_con_sintomi']
D2 = df['terapia_intensiva']
D3 = df['totale_ospedalizzati']
D4 = df['isolamento_domiciliare']
D5 = df['totale_positivi']
D6 = df['nuovi_positivi']
D7 = df['dimessi_guariti']
D8 = df['deceduti']
D9 = df['totale_casi']
D10 = df['tamponi']

# ## Statistical analysis with data taken from .csv

D1.values
D2.values
D3.values
D4.values
D5.values
D6.values
D7.values
D8.values
D9.values
D10.values

print('\t~ Analisi di Dati per quanto riguarda il SARS-CoV2 in Italia ~')
print('\n\t@Author: AlanTurista, alan.turista@gmail.com')
print('\n****************************************************************************************')
print("\n\tOggi è il",data1)
print('\n****************************************************************************************')
for val in D9:
    print("\n\t1. I casi totali sono:",val)

a = (100*D9)/60243406
for val in a:
    print('\n\t\t1.1. È stato infettato il','{0:.2f}'.format(val),'% della popolazione.')

for val in D7:
    print("\n\t2. I guariti sono:",val)

b = (100*D7)/D9
for val in b:
    print('\n\t\t2.1. Sono stati guariti il','{0:.2f}'.format(val),'%')

for val in D8:
    print("\n\t3. I deceduti sono:",val)
    
c = (100*D8)/D9
for val in c:
    print("\n\t\t3.1. Il tasso di mortalità è pari a",'{0:.2f}'.format(val),"%.")
    
for val in D2:
    print('\n\t4. I posti di terapia intensiva occupati sono:',val)

d = (100*D2)/5324
for val in d:
    print('\n\t\t4.1. È occupato il','{0:.2f}'.format(val),'% dei posti di terapia intensiva')

for val in D3:
    print('\n\t5. Gli ospedalizzati sono:',val)

e = (100*D3)/D9
for val in e:
    print('\n\t\t5.1. Sono ospedalizzati il','{0:.2f}'.format(val),'% del totale')

for val in D4:
    print('\n\t6. In isolamento domiciliare sono:',val)

f = (100*D4)/D9
for val in f:
    print('\n\t\t6.1. In isolamento domiciliare è il','{0:.2f}'.format(val),'% dei casi')

for val in D5:
    print('\n\t7. Gli attivi sono:',val)

g = (100*D5)/D9
for val in g:
    print('\n\t\t7.1. Gli attivi è il','{0:.2f}'.format(val),'% dei casi')    

for val in D6:
    print('\n\t8. I nuovi attualmente positivi sono:',val)

h = (100*D6)/D9
for val in h:
    print('\n\t\t8.1. I nuovi attualmente positivi è il','{0:.2f}'.format(val),'% dei casi')    

for val in D1:
    print('\n\t9. I ricoverati con sintomi sono:',val)      
    
for val in D10:
    print("\n\t10. Il numero dei tamponi usati è:",val)    
    
j = (100*D9)/D10
for val in j:
    print('\n\t\t10.1. Il','{0:.2f}'.format(val),'% dei tamponi usati è stato positivo.')
    
print('\n****************************************************************************************\n\n')

int(input('PREMI INVIO PER USCIRE'))