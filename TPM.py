# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:59:24 2022

@author: elbys
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates

#serie de TPM
tpm = pd.read_excel('https://cdn.bancentral.gov.do/documents/estadisticas/sector-monetario-y-financiero/documents/Serie_TPM.xlsx?v=1656977733786?v=1656977733789',
                    skiprows = 5,
                    skipfooter= 2,
                    usecols = 'C',
                    names = ['TPM'])

tpm['TPM'] = tpm['TPM'] * 100

date_tpm = pd.date_range(start = "2004-01-01", periods= len(tpm), freq='M')

tpm['Fecha'] = date_tpm
tpm.set_index("Fecha", inplace= True)

#serie de tasa pasiva

#tasa_pasiva_raw = pd.read_excel('https://cdn.bancentral.gov.do/documents/estadisticas/sector-monetario-y-financiero/documents/tbm_pasivad.xlsx?v=1657066533769?v=1657066533774', skiprows = 6, usecols = "J")

# PLOTTING

fig = plt.figure(figsize=(20,10))

ax0 = fig.add_subplot(1, 1, 1)

tpm.tail(36).plot(kind="line",
                  ax = ax0)

ax0.set_title('Tasa de Politica Monetaria', fontsize = 18, ha= 'center')
