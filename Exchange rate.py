# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:44:16 2022

@author: elbys
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

#Tipo de cambio
tipodecambio = pd.read_excel('https://cdn.bancentral.gov.do/documents/estadisticas/mercado-cambiario/documents/TASA_DOLAR_REFERENCIA_MC.xls?v=1627915152254', 
                             sheet_name = "FPMensual", 
                             skiprows = 2,
                             usecols = "A:D",
                             names = ['Año', 'Mes', 'Compra', 'Venta'])

#Creo lista con fechas de frecuencia mensual y con el rango de mi dataframe
datetc = pd.date_range(start = "1991-01-01", periods= len(tipodecambio), freq='M')

tipodecambio.drop(["Año", "Mes", "Compra"], axis=1, inplace=True)

tipodecambio["Mes"] = datetc

tipodecambio.set_index("Mes", inplace = True)

tipodecambio["Cambio Interanual"] = tipodecambio.pct_change(periods = 12) * 100

tc48 = tipodecambio["Venta"].tail(48)
tcinter48  = tipodecambio["Cambio Interanual"].tail(48)

#Plotting

fig = plt.figure() # create figure

ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2, 2) # add subplot 2 (1 row, 2 columns, second plot)

plt.style.use("ggplot")

# Subplot 1: line plot
tc48.plot(kind='line',
          figsize=(15,6),
          color = "slategrey",
          ax=ax0) # add to subplot 1

ax0.set_title('Tipo de cambio DOP/USD', fontsize=16, ha='center')
ax0.set_xlabel('Mes', fontsize=12, ha='center')
ax0.set_ylabel('DOP/USD', fontsize=16, ha='center')

# Subplot 2: Line plot
tcinter48.plot(kind='line',  
               figsize=(15, 6),
               color = "darkgreen",
               ax=ax1)

ax1.set_title ('Variacion Interanual del Tipo de Cambio', fontsize=16, ha='center')
ax1.set_ylabel('Porcentaje (%)', fontsize=12, ha='center')
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.axhline(y=0, color='black', linestyle='-')
ax1.set_xlabel('Mes', fontsize=16, ha='center')

plt.show()