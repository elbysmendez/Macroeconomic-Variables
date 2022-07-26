# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:52:16 2022

@author: elbys
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data_embi = "https://cdn.bancentral.gov.do/documents/entorno-internacional/documents/Serie_Historica_Spread_del_EMBI.xlsx?v=1650556499744"

#Building DataFrame

embi = pd.read_excel(data_embi,
                     skiprows=(1))
embi.set_index('Fecha', inplace = True)

embi_rd_latam = embi[{'Global', 'LATINO','REP DOM'}]

#Formato de axis X = fecha

fmt_fecha_embi = mdates.DateFormatter('%b-%Y')

#plotting

fig = plt.figure(figsize=(12, 10))

ax0 = fig.add_subplot(1,1,1)

embi_rd_latam.tail(400).plot(kind = "line",
                   ax=ax0)
ax0.set_title('EMBI')
ax0.set_ylabel('Porcentaje')
ax0.xaxis.set_major_formatter(fmt_fecha_embi)

plt.show()