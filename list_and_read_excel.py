from os import listdir
from os.path import isfile, join

arr = listdir('./')
arr = list(filter(lambda x: x.find('xlsx')>=0,arr))
name_arr = list(filter(lambda x:x.find('~$')<0, arr ))

import pandas as pd

ef_arr = list(map(pd.ExcelFile, name_arr))
df_arr = list(map(lambda x:x.parse(x.sheet_names[0],dtype=object), ef_arr))
