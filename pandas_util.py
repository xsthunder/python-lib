from functools import reduce
import pandas
def merge_sub_sheets(excel_file):
    assert isinstance(excel_file, pandas.io.excel.ExcelFile) 
    sheet_names = excel_file.sheet_names
    dfs = list(map(excel_file.parse, sheet_names))
    return reduce(lambda x,y: x.append(y), dfs)