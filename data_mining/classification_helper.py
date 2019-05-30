
OUTPUT2ONEHOT_FUNC=None

from sklearn.metrics import classification_report
def __classification_helper(y_true, model, X, output2onehot, y_predict):
    # np.ndarray != None cause [True, False,...]
    # None is None == True
    y_true_onehot = output2onehot(y_true) if output2onehot is not None else y_true
    y_predict = model.predict(X) if model is not None and X is not None else y_predict
    y_predict_onehot = output2onehot(y_predict) if output2onehot != None else y_predict
    return y_true_onehot, y_predict_onehot
    
def classification_report_helper(y_true, model=None, X=None,  output2onehot=OUTPUT2ONEHOT_FUNC, y_predict=None):
    """
    model.predict(X) as y_predict if model and X exist
    if OUTPUT2ONEHOT_FUNC == None, don't convert
    """
    y_true_onehot, y_predict_onehot=__classification_helper(y_true, model, X, output2onehot, y_predict)
    return classification_report(y_true_onehot, y_predict_onehot)
def classification_precision_helper(y_true, model=None, X=None,  output2onehot=OUTPUT2ONEHOT_FUNC, y_predict=None):
    """
    model.predict(X) as y_predict if model and X exist
    if OUTPUT2ONEHOT_FUNC == None, don't convert
    """
    y_true_onehot, y_predict_onehot=__classification_helper(y_true, model, X, output2onehot, y_predict)
    
    y_true_sparse_int = one_hot_predict_labels2neat_sparse_int(y_true_onehot)
    y_predict_sparse_int = one_hot_predict_labels2neat_sparse_int(y_predict_onehot)
    
    return sum(y_true_sparse_int==y_predict_sparse_int)/len(y_predict_sparse_int )
