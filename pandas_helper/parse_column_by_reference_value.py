def parse_val_by_reference_value(to_be_parsed, rv):
    """
    return 1 if in range 0 otherwise
    rv accept format like "<4.5", "4.3-90.0"
    """
    one = np.int(1)
    zero = np.int(0)
    assert isinstance(to_be_parsed, np.float)
    if(np.isnan(to_be_parsed)): return np.nan
    if(rv[0] == '<'):
        val = np.float64(rv[1:])
        if(to_be_parsed < val): return zero
        else :return one
    if(rv.find('-')>0):
        rv = rv.split('-')
        assert len(rv)==2
        lower,upper = map(np.float, rv)
        if(lower <= to_be_parsed and to_be_parsed <= upper): return zero
        else :return one
        
def parse_column_by_reference_value(sr, rv):
    assert isinstance(sr, pd.Series)
    assert isinstance(rv, str)
    return list(map(lambda x: parse_val_by_reference_value(x,rv), sr.values))
