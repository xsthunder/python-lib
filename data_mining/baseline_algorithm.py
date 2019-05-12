import copy
import numpy as np
from tqdm import tqdm

def random_shuffle(test_labels):
    """
    @params test_labels: array-like object
    @returns copy of test_labels with random shuffle
    ----
    test_labels_copy = random_shuffle(test_labels)
    """
    test_labels_copy = copy.copy(test_labels)
    np.random.shuffle(test_labels_copy)
    return test_labels_copy

def random_shuffle_baseline(test_labels, epochs=1):
    """
    @params test_labels must be interger or string
    @returns classification acc of random shuffle baseline algorithm
    ------
    labels.astype('int64')
    classification_acc_on_random_algorithm(labels)
    """
    def f():
        test_labels_copy = random_shuffle(test_labels)
        return float(np.sum(np.array(test_labels) == np.array(test_labels_copy))) / len(test_labels)
    return sum(f() for i in tqdm(range(epochs)))/epochs

from pandas import Series

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

def one_shoot_baseline(labels,ascending=False ):
    """
    @params labels array-like, must be array of sparse interger or string
    @returns (counts of each value sort in increasing order by default, accuracy by oneshoot baseline algorithm)
    -----
    labels.astype('int64')
    one_shoot_baseline(labels)
    """
    srvc = labels_value_counts(labels, ascending) # from large to small
    single_spot_shooter = srvc.max()/len(labels)
    return srvc, single_spot_shooter
