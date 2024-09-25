import numpy as np
import mne
import pandas as pd
edf = mne.io.read_raw_edf('D:\\Lab\\Москва 25.09.2023\\Cohort 1\\table 1\\user_01\\2023.09.21-20.43.30.628.edf')
header = ','.join(edf.ch_names)
np.savetxt('D:\\Lab\\Москва 25.09.2023\\Cohort 1\\table 1\\user_01\\your_csv_file.csv', edf.get_data().T, delimiter=',', header=header)

