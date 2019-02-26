import json
def save_as_json(obj,file_name, ensure_ascii=False):
    f = open(file_name,'w')
    json.dump( obj, fp=f,ensure_ascii=ensure_ascii)
