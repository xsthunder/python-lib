import numpy
import pandas
def isnan(x, empty_str_as_nan = True, on_unknow_type = True):
    if( isinstance(x, str) ):
        if(empty_str_as_nan):
            return x == ''
        else :
            return False
    if( isinstance(x, numpy.float) ):
        return numpy.isnan(x)
    return on_unknow_type

def filter_nan(df,empty_str_as_nan = True, on_unknow_type = True):
    """
    or use df.dropna()
    return series indicating dataframe consisting rows which don't contain nan value
    you may use df[ret]
    support array bool op such as &
    """
    assert isinstance(df, pandas.DataFrame), "wrong type:%s, expected %s"%(type(df), pandas.DataFrame)
    return df.apply(lambda sr: all(map(lambda x:~is_nan(x,empty_str_as_nan,on_unknow_type ),  list(sr))), axis=1)

def filter_has_nan(df,empty_str_as_nan = True, on_unknow_type = True):
    """
    return series indicating dataframe consisting rows which contain any nan value
    you may use df[ret]
    support array bool op such as &
    """
    assert isinstance(df, pandas.DataFrame), "wrong type:%s, expected %s"%(type(df), pandas.DataFrame)
    return df.apply(lambda sr: any(map(lambda x:is_nan(x,empty_str_as_nan,on_unknow_type ),  list(sr))), axis=1)

