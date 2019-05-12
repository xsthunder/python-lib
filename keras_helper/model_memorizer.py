import keras
from keras import models
import os
import pickle
import numpy

class ModelMemorizer:
    """
    for keras instance
    mm = ModelMemorizer('test')
    mm.dump(model, history.history)
    (model, history_dict) = mm.load()
    """
    def __init__(self, name, path='./model-memorizer', standalone_path=True, mkdir=True):
        self.name = name
        if standalone_path:
            path='%s/%s'%(path, name)
        self.path = path
        if mkdir:
            os.makedirs(self.path, exist_ok=True)
        self.model_path = '%s/%s.model.h5'%(path, name)
        self.history_dict_path = '%s/%s.history_dict.pickle'%(path, name)
        
    def mkdir(self):
        os.makedirs(self.path, exist_ok=True) # python above 3.4
        
    def dump_history_dict(self, history_dict):
        assert isinstance(history_dict, dict)
        f = open(self.history_dict_path, 'wb')
        pickle.dump(history_dict, f)
        f.close()
        
    def load_history_dict(self):
        f = open(self.history_dict_path, 'rb')
        history_dict = pickle.load( f)
        f.close()
        return history_dict
    
    def dump_model(self, model):
        assert isinstance(model, keras.engine.sequential.Sequential)
        model.save(self.model_path)
        
    def load_model(self):
        return models.load_model(self.model_path)
    
    def dump(self, model, history_dict):
        self.dump_history_dict(history_dict)
        self.dump_model(model)
    
    def load(self):
        return self.load_model(), self.load_history_dict()
