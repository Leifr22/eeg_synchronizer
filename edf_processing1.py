# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:42:22 2023

@author: demian
"""

#%%
# Файл eeg для обрбаботки
enter1 = r'C:\\Users\\Guest\\Desktop\\test2\\2023.10.05-15.55.50.519.edf'
enter2 = r'C:\\Users\\Guest\\Desktop\\test2\\2023.10.05-15.58.31.786.edf'





import numpy as np
import mne
import pandas as pd



#%%

edf = mne.io.read_raw_edf(enter1)

header = ','.join(edf.ch_names)

np.savetxt('C:\\Users\\Guest\\Desktop\\test2\\test.csv', edf.get_data().T, delimiter=',', header=header)
data=pd.read_csv('C:\\Users\\Guest\\Desktop\\test2\\test.csv')
print(data)




#%%
edf2 = mne.io.read_raw_edf(enter2)
header= ','.join(edf2.ch_names)
np.savetxt('C:\\Users\\Guest\\Desktop\\test2\\test2.csv', edf2.get_data().T, delimiter=',', header=header)
data2=pd.read_csv('C:\\Users\\Guest\\Desktop\\test2\\test2.csv')
print(data2)

#%%
time_per_row1=106/13250
time_per_row2=115/14375
mid_row_time=(time_per_row1+time_per_row2)/2
offset_start=77/mid_row_time
offset_end=79/mid_row_time
gap_lines=int(102/mid_row_time)

data=data[int(offset_start):]
data2=data2[:len(data2)-int(offset_end)]





#%%
gap=pd.DataFrame(np.nan,index=range(gap_lines),columns=data.columns)
data3=pd.concat([data,gap,data2],ignore_index=True)
data3.to_csv('C:\\Users\\Guest\\Desktop\\test2\\test_united.csv')
print(data3)
