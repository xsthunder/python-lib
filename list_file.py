from os import listdir
from os.path import isfile, join

arr = listdir('./')
arr = list(filter(lambda x: x.find('xlsx')>=0,arr))
name_arr = list(filter(lambda x:x.find('~$')<0, arr ))
