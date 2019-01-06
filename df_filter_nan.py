import numpy
import pandas
def filter_nan(df):
  """
  return dataframe consisting rows which don't contain nan value
  """
  assert isinstance(df, pandas.DataFrame), "wrong type:%s, expected %s"%(type(df), pandas.DataFrame)
  return df[df.apply(lambda sr: all(map(lambda x:~numpy.isnan(x),  list(sr))), axis=1)]

