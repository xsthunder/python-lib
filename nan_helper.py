import numpy
import pandas
def filter_nan(df):
    """
    return series indicating dataframe consisting rows which don't contain nan value
    you may use df[ret]
    support array bool op such as &
    """
    assert isinstance(df, pandas.DataFrame), "wrong type:%s, expected %s"%(type(df), pandas.DataFrame)
    return df.apply(lambda sr: all(map(lambda x:~numpy.isnan(x),  list(sr))), axis=1)

def filter_has_nan(df):
    """
    return series indicating dataframe consisting rows which contain any nan value
    you may use df[ret]
    support array bool op such as &
    """
    assert isinstance(df, pandas.DataFrame), "wrong type:%s, expected %s"%(type(df), pandas.DataFrame)
    return df.apply(lambda sr: any(map(lambda x:numpy.isnan(x),  list(sr))), axis=1)

