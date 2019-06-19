import pandas as pd
def rename_column(df, name, new_name):
    assert isinstance(name, str)
    assert isinstance(new_name, str)
    assert isinstance(df, pd.DataFrame)
    rename_dic = {}
    rename_dic = {name:new_name}# notes difference with {name, new_name}
    df = df.rename(index=str, columns=rename_dic)
    return df
