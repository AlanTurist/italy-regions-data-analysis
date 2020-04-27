import datetime
data = datetime.datetime.now()
data1 = data.strftime("%d-%m-%Y %H:%M:%S")

import pandas as pd
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv'
df = pd.read_csv(url,index_col=0, sep=",")

def regione(reg, x, y):
    reg1 = df.iloc[x]
    D1 = reg1['ricoverati_con_sintomi']
    D2 = reg1['terapia_intensiva']
    D3 = reg1['totale_ospedalizzati']
    D4 = reg1['isolamento_domiciliare']
    D5 = reg1['totale_positivi']
    D7 = reg1['dimessi_guariti']
    D8 = reg1['deceduti']
    D9 = reg1['totale_casi']
    D10 = reg1['tamponi']
    
    print('\n\t~ Analisi di Dati di SARS-CoV2 in',reg,'~')
    print('\n\t@Author: AlanTurista, alan.turista@gmail.com')
    print('*'*110)    
    print("\n\tOggi è il",data1)
    print('\n')
    print("*"*50,reg,"*"*50)

    print("\n\t1. I casi totali in sono:",D9)
    a = (100*D9)/y
    print('\n\t\t1.1. È stato infettato il','{0:.2f}'.format(a),'% della regione.')
    
    print("\n\t2. I guariti sono:",D7)
    b = (100*D7)/D9
    print('\n\t\t2.1. Sono stati guariti il','{0:.2f}'.format(b),'%')
    
    print("\n\t3. I deceduti sono:",D8)
    c = (100*D8)/D9
    print("\n\t\t3.1. Il tasso di mortalità è pari a",'{0:.2f}'.format(c),"%.")
    
    print('\n\t4. I posti di terapia intensiva occupati sono:',D2)
    d = (100*D2)/5324
    print('\n\t\t4.1. È occupato il','{0:.2f}'.format(d),'% del totale dei posti di terapia intensiva')
    
    print('\n\t5. Gli ospedalizzati sono:',D3)
    e = (100*D3)/D9
    print('\n\t\t5.1. Sono stati ospedalizzati il','{0:.2f}'.format(e),'% dei casi')
    
    print('\n\t6. In isolamento domiciliare sono:',D4)
    f = (100*D4)/D9
    print('\n\t\t6.1. In isolamento domiciliare è il','{0:.2f}'.format(f),'% dei casi')
    
    print('\n\t7. I positivi sono:',D5)
    g = (100*D5)/D9
    print('\n\t\t7.1. I positivi sono il','{0:.2f}'.format(g),'% dei casi')
        
    print("\n\t8. Il numero dei tamponi usati è:",D10)    
    h = (100*D9)/D10
    print('\n\t\t8.1. Il','{0:.2f}'.format(h),'% dei test è stato positivo.')

    print('\n\t10. I ricoverati con sintomi sono:',D1)
    print('\n')
    print('*'*110)