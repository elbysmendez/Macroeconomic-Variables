# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:41:49 2022 

@author: elbys
"""

import pandas as pd
import matplotlib.pyplot as plt

# IMAE

#Data
crecimiento_imae = pd.read_excel("https://cdn.bancentral.gov.do/documents/estadisticas/sector-real/documents/imae.xlsx?v=1643308962694?v=1643308962698",
                     skiprows=8,
                     skipfooter=1,
                     )

crecimiento_imae.drop(['Unnamed: 0', 'Unnamed: 2', 'Acumulada', 'Promedio 12 meses', 'Unnamed: 6', 'Respecto al período anterior', 'Interanual.1', 'Acumulada.1', 'Promedio 12 meses.1', 'Unnamed: 11', 'Respecto al período anterior.1', 'Acumulada.2', 'Promedio 12 meses.2'],
          axis=1,
          inplace = True)

crecimiento_imae.dropna(inplace=True)
crecimiento_imae.rename(columns={"Unnamed: 1": "Fecha", "Interanual": "Serie Original","Interanual.2": "Tendencia Ciclo" }, inplace=True)

dateimae = pd.date_range(start = "2008-01-01", periods= len(crecimiento_imae), freq='M')

crecimiento_imae["Fecha"] = dateimae

crecimiento_imae.set_index("Fecha", inplace=True)

#Plotting just the last 3 years

imae_3y = crecimiento_imae.tail(36)

fig = plt.figure()

plt.style.use("tableau-colorblind10")

ax0 = fig.add_subplot(2, 1, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(2, 1, 2) # add subplot 2 (1 row, 2 columns, second plot)

#Plot imae original
imae_3y["Serie Original"].plot(kind = "bar", 
                               figsize = (15,20), 
                               ax = ax0)

ax0.set_title('Crecimiento interanual de la actividad economica (IMAE)', fontsize=20, ha='center')
ax0.set_xlabel('Mes', fontsize=16, ha='center')
ax0.set_ylabel("Porcentaje", fontsize=14, ha='center')
ax0.axhline(y=0, color='gray', linestyle='-')

#Plot tendencia ciclo
imae_3y["Tendencia Ciclo"].plot(kind = "line", 
                                color="red", 
                                figsize = (15,20), 
                                ax = ax1, 
                                sharex = ax0)

ax1.set_title("IMAE tendencia ciclo", fontsize=20, ha='center')
ax1.set_xlabel('Mes', fontsize=16, ha='center')
ax1.set_ylabel("Porcentaje", fontsize=14, ha='center')
ax1.axhline(y=0, color='gray', linestyle='-')

#plt.show()