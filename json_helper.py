import json
def save_as_json(obj,file_name, ensure_ascii=False):
    f = open(file_name,'w')
    json.dump( obj, fp=f,ensure_ascii=ensure_ascii)
def sample_dict(dic, count=5):
    return list(dic.items())[:count]
def load_as_json(file_name):
    jy = json.load(open(file_name))
