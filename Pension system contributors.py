# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 09:51:40 2022

@author: elbys
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
    
datasipen = 'https://www.sipen.gob.do/index.php/descarga/estadistica-previsional_2022_06_20220708120815.xls'

#Data cotizantes
cotizantes = pd.read_excel(datasipen,
                           sheet_name = "TOTALES",
                           skiprows = 7,
                           usecols = "B",
                           names = ["Cotizantes"])

datecotizantes = pd.date_range(start = "2004-01-01", periods= len(cotizantes), freq='M')

cotizantes['Mes'] = datecotizantes

cotizantes.set_index('Mes', inplace = True)

cotizantes48 = cotizantes.tail(60)

dcotizantes = cotizantes.diff(periods = 1)

diffcotizantes = dcotizantes.tail(12)
myFmt = mdates.DateFormatter('%b')

#diffcotizantest = diffcotizantes.transpose()

#Cotizantes por salario
cotizantes_salario = pd.read_excel(datasipen,
                           sheet_name = "Por SALARIO",
                           skiprows = 3,
                           usecols = "B:K")

cotizantes_salario.dropna(inplace = True)

cotizantes_salario.set_index('Mes', inplace=True)

dcotizantes_salario = cotizantes_salario.diff(periods = 12)

diffsalario = dcotizantes_salario.tail(1)

diffsalariot = diffsalario.transpose()

cotizantes_4_6_salarios = dcotizantes_salario["4-6"].tail(24)
datecotizantes46 = pd.date_range(start = "2020-06-01", periods= len(cotizantes_4_6_salarios), freq='M')
dfcotizantes46salarios = pd.DataFrame(cotizantes_4_6_salarios)
dfcotizantes46salarios["Fecha"] = datecotizantes46
dfcotizantes46salarios.set_index("Fecha", inplace = True)

#Cotizantes por edad
cotizantes_edad = pd.read_excel(datasipen,
                           sheet_name = "Por EDAD",
                           skiprows = 3,
                           usecols = "B:L")

cotizantes_edad.set_index('Mes', inplace=True)

dcotizantes_edad = cotizantes_edad.diff(periods = 12)

diffedad = dcotizantes_edad.tail(1)

diffedadt = diffedad.transpose()

#Plotting

fig, axd = plt.subplot_mosaic([['up', 'up'],
                               ['lowleft', 'lowright']], 
                              figsize=(20, 10))

# Subplot 1: Cambio por edad
diffedadt.plot(kind='bar', 
               color = "#838B8B", 
               ax= axd['lowleft'], 
               legend = None) 

axd['lowleft'].set_title ('Cambio en los cotizantes segun rango de edad, interanual')
axd['lowleft'].set_ylabel('Personas')
axd['lowleft'].set_xlabel('Rango de edad')
axd['lowleft'].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

# Subplot 2: Cambio por edad
diffsalariot.plot(kind='bar', 
                  color = "#C1CDCD",  
                  ax=axd['lowright'], 
                  legend = None) 

axd['lowright'].set_title ('Cambio en los cotizantes segun rango de salario minimo, interanual')
axd['lowright'].set_ylabel('Personas')
axd['lowright'].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
axd['lowright'].set_xlabel('Rango de salario minimo')

# Subplot 3: Evolucion cotizantes
cotizantes48.plot(kind='line',
                  color='#008B00', 
                  ax = axd['up'],
                  legend = None) 

axd['up'].set_title('Cantidad de cotizantes en el Sistema de Seguridad Social')
axd['up'].set_xlabel('Mes')
axd['up'].set_ylabel('personas')
axd['up'].set_ylim(1000000, 2200000)
axd['up'].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) #formato de axis Y, pone comas como separador de miles

plt.subplots_adjust(wspace = 0.15, hspace = 0.5)

plt.show()
