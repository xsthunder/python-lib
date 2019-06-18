import pandas as pd
def merge_df_on_index(df1, df2, how='inner'):
  return pd.merge(df1, df2,  left_index=True, right_index=True, how=how)
