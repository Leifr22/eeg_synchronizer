# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:42:22 2023

@author: demian
"""

#%%
# Файл eeg для обрбаботки
enter1 = r'C:\\Users\\Guest\\Desktop\\test3\\2023.10.05-16.13.59.087.edf'
enter2 = r'C:\\Users\\Guest\\Desktop\\test3\\2023.10.05-16.16.40.868.edf'





import numpy as np
import mne
import pandas as pd



#%%

edf = mne.io.read_raw_edf(enter1)

header = ','.join(edf.ch_names)

np.savetxt('C:\\Users\\Guest\\Desktop\\test3\\test.csv', edf.get_data().T, delimiter=',', header=header)
data=pd.read_csv('C:\\Users\\Guest\\Desktop\\test3\\test.csv')
print(data)




#%%
edf2 = mne.io.read_raw_edf(enter2)
header= ','.join(edf2.ch_names)
np.savetxt('C:\\Users\\Guest\\Desktop\\test3\\test2.csv', edf2.get_data().T, delimiter=',', header=header)
data2=pd.read_csv('C:\\Users\\Guest\\Desktop\\test3\\test2.csv')
print(data2)
#%%
time_per_row1=80/10000
time_per_row2=75/9375
mid_row_time=(time_per_row1+time_per_row2)/2
lag_start=int(70/mid_row_time)
lag_end=int(68/mid_row_time)
gap_lines=int(81/mid_row_time)

#%%
gap= pd.DataFrame([float('nan')] * data.shape[1], index=data.columns).transpose()
start_gap = pd.concat([gap] * lag_start, ignore_index=True) 
end_gap = pd.concat([gap] * lag_end, ignore_index=True)
mid_gap = pd.concat([gap] * gap_lines, ignore_index=True)
data3 = pd.concat([start_gap, data, mid_gap, data2, end_gap], ignore_index=True)
data3.to_csv('C:\\Users\\Guest\\Desktop\\test3\\test_united.csv')
print(data3)

