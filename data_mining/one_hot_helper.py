from pandas import Series
def one_hot_labels2neat_sparse_label(labels):
    """
    get neat interger class number by argmax()
    @params labels: np.ndarray
    """
    arr_label = np.apply_along_axis(lambda row:row.argmax(), 1, labels,)
    return arr_label

def one_hot_predict_labels2value_count(labels):
    """
    get neat interger class number by argmax(), and value count then
    @params labels: np.ndarray
    """
    return labels_value_counts(one_hot_predict_labels2neat_sparse_label(labels))

def one_hot_model2value_count(model, X):
    """
    predict and value count the predicted class
    """
    return one_hot_labels2value_count(model.predict(X))
   
   
# FIXME duplicated in baseline_algorithm
def labels_value_counts(labels, sort_values=True, ascending=False):
    """
    @params labels: array-like, must be array of sparse interger or string
    @params sort_values: bool, wheter to sort label types by theirs count
    @params ascending: bool, indicates how to sort sort label by theirs count
    @returns pd.Series of value count of labels
    -----
    labels.astype('int64')
    labels_vc = label_value_counts(labels)
    lalabels_vc.argmax(), labels_vc.max() # (max label type, its count)
    """
    sr = Series(labels)
    srvc = sr.value_counts()
    if(sort_values):srvc=srvc.sort_values(ascending=ascending)
    return srvc
