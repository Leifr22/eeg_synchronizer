import numpy as np
import mne
import pandas as pd
edf = mne.io.read_raw_edf('dir_to_edffile')
header = ','.join(edf.ch_names)
np.savetxt('your_csv_file.csv', edf.get_data().T, delimiter=',', header=header)

