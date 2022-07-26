# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:45:55 2022

@author: elbys
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib as mpl

#MENSUAL
llegada_turistas_mensual = pd.read_excel('https://cdn.bancentral.gov.do/documents/estadisticas/sector-turismo/documents/lleg_total.xls?v=1651156776256',
                                 skiprows = 7,
                                 usecols='B',
                                 sheet_name = 'Llegada Total 93-22')

llegada_turistas_mensual.dropna(inplace=True)

fecha_serie_mensual = pd.date_range(start = "1993-01-01", periods= len(llegada_turistas_mensual), freq='M')

llegada_turistas_mensual['Fecha'] = fecha_serie_mensual
llegada_turistas_mensual.set_index('Fecha', inplace = True)

llegada_turistas_mensual['Var. interanual'] = llegada_turistas_mensual['Mensual'].pct_change(periods = 12) * 100

#ANNUAL
data_anual = pd.read_excel('https://cdn.bancentral.gov.do/documents/estadisticas/sector-turismo/documents/lleg_total.xls?v=1651156776256',
                                 skiprows = 5,
                                 usecols = "A:AD",
                                 skipfooter = 42,
                                 sheet_name = '1993 - 2022')
data_anual.rename({"DETALLE": "Año"}, axis = "columns", inplace=True)
data_anual.drop([0], inplace =True)
data_anual.set_index("Año", inplace = True)          

llegada_turistas_anual = data_anual.transpose()
llegada_turistas_anual['Var. interanual'] = llegada_turistas_anual['TOTAL'].pct_change(periods = 1) * 100

#ingresos por turismo
turismo_valor = pd.read_excel('https://cdn.bancentral.gov.do/documents/estadisticas/sector-turismo/documents/turismo_valor.xls?v=1652724626913',
                              skiprows=6,
                              skipfooter=194)

ingresos_turismo = turismo_valor[['Anual', 'Unnamed: 3']]
ingresos_turismo.set_index("Anual", inplace = True)
ingresos_turismo.rename(columns={'Unnamed: 3': 'Ingresos por turismo'}, inplace=True)

ingresos_turismo["Variacion %"]=ingresos_turismo['Ingresos por turismo'].pct_change(periods = 1) * 100

#Plotting

fig, axd = plt.subplot_mosaic([['upleft', 'upright'],
                               ['lowleft', 'lowright']], 
                              figsize=(30, 12))

#plt.style.use("fivethirtyeight")

#Plot ['1']
llegada_turistas_mensual['Mensual'].tail(60).plot(kind = 'line',
                                                  ax = axd['upleft'],
                                                  color = 'darkgreen')

axd['upleft'].set_title('Llegada mensual de pasajeros via aerea', fontsize = 20, ha="center")
axd['upleft'].set_ylabel('Personas', fontsize = 12, ha = 'center')
axd['upleft'].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

#Plot ['2']
llegada_turistas_anual["TOTAL"].tail(6).plot(kind = "bar",
                                             ax = axd['upright'],
                                             color = 'darkgreen')

axd['upright'].set_title('Llegada total de pasajeros via aerea por año', fontsize = 20, ha='center')
axd['upright'].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

#Plot ['3']
ingresos_turismo['Ingresos por turismo'].tail(10).plot(kind = 'bar',
                                                       ax = axd['lowleft'],
                                                       color="slategrey")

axd['lowleft'].set_title('Ingresos por turismo del sector privado', fontsize = 18, ha='center')
axd['lowleft'].yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

#Plot['4']
ingresos_turismo['Variacion %'].tail(10).plot(kind = 'line',
                                              ax = axd['lowright'],
                                              color = 'seagreen')

axd['lowright'].set_title('Cambio anual en los ingresos por turismo', fontsize = 18, ha='center')
axd['lowright'].set_ylabel('porcentaje', fontsize = 14, ha='center')

plt.subplots_adjust(wspace = 0.1, hspace = 0.25)