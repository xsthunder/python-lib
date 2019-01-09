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
    ef_arr = list(map(pd.ExcelFile, path_arr))

