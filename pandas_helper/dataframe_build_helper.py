def dataFrameFromIndexDict(index_dict_array):
    """
    use dict to build a dataframe with string as index
    @parma index_dict_array: Array<string, dict>
    """
    return pd.DataFrame([tp[1] for tp in index_dict_array], index=[tp[0] for tp in index_dict_array])
