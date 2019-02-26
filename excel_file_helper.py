from functools import reduce
import pandas

from os import listdir
from os.path import isfile, join
import pandas as pd

def read_excel_file_name(dir = './', contains=['.xlsx'], notcontains=['~$']):
    arr = listdir(dir)
    for s in contains:
        arr = list(filter(lambda x: x.find(s)>=0,arr))
    for s in notcontains:
        arr = list(filter(lambda x:x.find('~$')<0, arr ))
    name_arr = arr
    path_arr = list(map(lambda x:dir+x, name_arr))
    return path_arr,name_arr

def read_ef_arr(path_arr):
    return list(map(pd.ExcelFile, path_arr))

def merge_sheets(excel_file):
    assert isinstance(excel_file, pandas.io.excel.ExcelFile) 
    sheet_names = excel_file.sheet_names
    dfs = list(map(excel_file.parse, sheet_names))
    return reduce(lambda x,y: x.append(y), dfs)

def read_df_arr(ef_arr):
    return list(map(lambda x:x.parse(x.sheet_names[0],dtype=object), ef_arr))
