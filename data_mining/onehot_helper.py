from pandas import Series
import numpy as np
from keras.utils.np_utils import to_categorical

def neat_sparse_label2onehot(y):
    return to_categorical(y)

def onehot_labels2neat_sparse_label(labels):
    """
    get neat interger class number by argmax()
    @params labels: np.ndarray
    """
    arr_label = np.apply_along_axis(lambda row:row.argmax(), 1, labels,)
    return arr_label

def onehot_labels2value_count(labels):
    """
    get neat interger class number by argmax(), and value count then
    @params labels: np.ndarray
    """
    return labels_value_counts(onehot_labels2neat_sparse_label(labels))

def onehot_model2value_count(model, X):
    """
    predict and value count the predicted class
    """
    return onehot_labels2value_count(model.predict(X))


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


# start binary helper
def mutilclass2binary(y, threshold):
    tmp_test = np.apply_along_axis(np.argmax, -1, y)
    l = len(y)
#     print(l)
    y = np.zeros(shape=(l))
    for i in range(l):
        y[i] = 0 if tmp_test[i] <=threshold else 1
    return y

def binary_predict2onehot(binary_y):
    rounded_binary_y = np.apply_along_axis(np.round, -1, binary_y)
    l = len(binary_y)
    y = np.zeros(shape=(l, 2))
    for i,x in enumerate(rounded_binary_y):
        y[i][int(x)] = 1
    return y
# end binary helper

# start class regression helper

def onehot2regression(y):
    return one_hot_labels2neat_sparse_label(y)

def regression2onehot(regression_y, category_type=6):
    l = len(regression_y)
    zeroes_y = np.zeros(shape=(l, category_type))
    rounded_regression_y = np.apply_along_axis(np.round, -1, regression_y)
    for i in range(l):
        zeroes_y[i][int(rounded_regression_y[i])] = 1.0
    return zeroes_y
# start class regression helper

