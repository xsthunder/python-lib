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
    if(threshold < 0):
        return l
    else :
        return list(filter(lambda x: len(x) < threshold, l))

    
