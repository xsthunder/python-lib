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
    return [(<col_name>, <#value_type>, <column_value_type>),..]
    [
        ('img-path', 442, dtype('O')),
        ('keyned-position', 2, dtype('int64'))
    ]
    """
    assert isinstance(df, pandas.DataFrame)
    columns = df.columns if columns == None else columns
    def f(name_sr):
        name, sr = name_sr
        return name,len(sr.value_counts()), sr.dtype
    return list(map(f, df.items()))