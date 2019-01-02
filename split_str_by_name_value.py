import re
def split_str_by_name_value(s, optional_name_list= [
                            '虫卵',
                           '大便颜色',
                           '外观性状',
                          ] 
    , common_value_reg = '阴性|阳性|\d|<'):
    """
    split s which form are <name><value>
    first try to split by name in name_list first,
    then try value_regex to catch common pattern
    e.g.
    虫卵未见 -> ('虫卵','未见')
    红细胞（便）0 个/HP -> ('红细胞（便）','0 个/HP')
    """
    ret = re.search('|'.join(map(re.escape, optional_name_list)), s) # match by check type
    if ret is None:
        ret = re.search(r'阴性|阳性|\d|<', s) # match by value pattern
        assert ret is not None, "spliter for check_type and check_result is not working"
        start, end = (ret.start(), ret.end())
        _type = s[:start]
        result = s[ret.start():]
    else:# match by optional name list
        start, end = (ret.start(), ret.end())
        _type = ret.group()
        result = s[end:]
    return _type, result
