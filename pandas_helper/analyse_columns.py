import pandas
def analyse_columns(df, columns=None, threshold=-1):
    """
    filter len(df[column of columns].value_counts()) by threshold
    will not filter if threshold < 0
    reutrn arr: df[column].value_counts() of each column of columns in df
    """
    assert isinstance(df, pandas.DataFrame)
    columns = df.columns if columns == None else columns
    l = list(map(lambda x: df[x].value_counts(dropna=False), columns))
    if(threshold < 0): return l
    ret = list(filter(lambda x: len(x) < threshold, l))
    return ret

def value_value_counts(df, columns=None,):
    """
    meta information about column
    return [(<col_name>, <#value_type>, <column_index_type>, <column_values_type>),..] # type may not always correct
    [
        ('img-path', 442, dtype('O')),
        ('keyned-position', 2, dtype('int64'))
    ]
    """
    assert isinstance(df, pandas.DataFrame)
    columns = df.columns if columns == None else columns
    def f(name_sr):
        name, sr = name_sr
        return name,len(sr.value_counts()), sr.index.dtype, sr.values.dtype
    return list(map(f, df.items()))

def filter_valid_column_names(df, nan_threshold = None):
    """
    return column names of column that has no more than nan_threshold value of nan, None or nat
    """
    assert isinstance(df, pandas.DataFrame)
    nan_threshold = len(df) if nan_threshold is None else nan_threshold
    def f(column_status): # nan count
        nansr = column_status[pd.isnull(column_status.index)] # see https://pandas.pydata.org/pandas-docs/stable/missing_data.html
        return np.sum(nansr.values)
    columns_status = analyse_columns(df, )
    valid_columns = list(filter(lambda l:f(l) < nan_threshold, columns_status))
    valid_columns_names = list(map(lambda x:x.name, valid_columns))
    return valid_columns_names
