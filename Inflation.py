# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:46:36 2022

@author: elbys
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib as mpl
import matplotlib.dates as mdates

#Inflacion
inflacion = pd.read_excel('https://cdn.bancentral.gov.do/documents/estadisticas/precios/documents/ipc_base_2019-2020.xls?v=1628089560244',
                          sheet_name = "IPC base 2019-2020",
                          skiprows = 6,
                          skipfooter = 3,
                          usecols = "D:F",
                          names = ["Var. mensual", "Var. con Dic", "Inflacion"])

inflacion.dropna(inplace=True)

dateipc = pd.date_range(start = "1984-01-01", periods= len(inflacion), freq='M')

inflacion['Fecha'] = dateipc

inflacion.set_index('Fecha', inplace = True)

inflacion_last_2y = inflacion.tail(48)
inflacion_last_2y.index = inflacion_last_2y.index.strftime('%Y-%m')

#Inflacion Subyacente
inflacion_subyacente = pd.read_excel('https://cdn.bancentral.gov.do/documents/estadisticas/precios/documents/ipc_subyacente_base_2019-2020.xlsx?v=1655672384017',
                                     skiprows = 28,
                                     skipfooter = 4,
                                     usecols = "F",
                                     names = ["I. Subyacente"])
inflacion_subyacente.dropna(inplace=True)

date_subyacente = pd.date_range(start = "2000-01-01", periods= len(inflacion_subyacente), freq='M')
inflacion_subyacente["Fecha"] = date_subyacente
inflacion_subyacente.set_index("Fecha", inplace = True)

#Salario

datasalario = 'https://www.sipen.gob.do/index.php/descarga/estadistica-previsional_2022_06_20220708121402.xls'

salario = pd.read_excel(datasalario,
                        skiprows = 4,   
                        usecols = "C", 
                        names = ["Salario"])

datesalario = pd.date_range(start = "2003-07-01", periods= len(salario), freq='M')
salario["Mes"] = datesalario
salario.set_index("Mes", inplace = True)
salario["Crecimiento anual"] = salario.pct_change(periods = 12) * 100
nivel_salario = pd.DataFrame(salario["Salario"].tail(48))
crecsalario = salario["Crecimiento anual"].tail(48)

#PLOTING

#Inflacion mensual
fig = plt.figure(figsize=(25, 7))

ax0 = fig.add_subplot(1, 3, 1) #(rows, columns, no. of plot)
ax1 = fig.add_subplot(1, 3, 2)
ax2 = fig.add_subplot(1, 3, 3)


plt.style.use('seaborn')

inflacion_last_2y["Var. mensual"].tail(12).plot(kind ='bar',
                                       ax=ax0,
                                       figsize = (25, 7),
                                       )

ax0.set_title('Inflacion mensual', fontsize=18, ha='center')
ax0.set_ylabel('Porcentaje (%)', fontsize=14, ha='center')

#Inflacion interanual y subyacente

nivel_precios = pd.DataFrame(data = None, 
                            columns = ['Inflacion', 'Inflacion subyacente'])

nivel_precios["Inflacion"] = inflacion["Inflacion"].tail(24)
nivel_precios["Inflacion subyacente"] = inflacion_subyacente["I. Subyacente"].tail(24)

nivel_precios.plot(kind ='line',
                   ax=ax1,
                   figsize = (25, 7)
                   )

ax1.set_title('Inflacion Interanual y subyacente', fontsize=18, ha='center')
ax1.set_ylabel('Porcentaje (%)', fontsize=14, ha='center')
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.axhline(y=4, color='gray', linestyle='-')
ax1.axhline(y=5, color='gray', linestyle='--')
ax1.axhline(y=3, color='gray', linestyle='--')
ax1.set_xlabel('Mes', fontsize=11, ha='center')

#Salario

crecsalario.plot(kind='line', 
                   color = "darkgreen", 
                   figsize=(25, 7), 
                   ax=ax2) # add to subplot 3

ax2.set_title ('Crecimiento del salario cotizable', fontsize=18, ha='center')
ax2.set_ylabel('Porcentaje (%)', fontsize=14, ha='center')
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
ax2.axhline(y=0, color='gray', linestyle='-')
ax2.set_xlabel('Mes', fontsize=11, ha='center')

