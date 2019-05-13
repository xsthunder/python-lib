import matplotlib.pyplot as plt
import numpy as np

def __smooth_curve(points, factor = 0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous*factor + point*(1-factor))
        else :
            smoothed_points.append(point)
    return smoothed_points

def graph_on_train_val_metric(history_dict, metric, smooth_curve=False, subplt=plt):
    """
    绘制训练和验证任意指标
    history = model.fit(...)
    ------
    %matplotlib inline
    plt = graph_on_train_val_metric(history_dict, 'loss') # 等价于 graph_on_train_val_loss(history_dict)
    plt.show()
    """
    metric_name = metric
    metric = history_dict[metric_name]
    val_metric = history_dict['val_%s'%metric_name]

    epochs = range(1, len(metric) + 1)

    if(smooth_curve):
        metric = __smooth_curve(metric)
        val_metric = __smooth_curve(val_metric)

    subplt.plot(epochs, metric, 'bo', label='Training %s'%metric_name)
    subplt.plot(epochs, val_metric, 'b', label='Validation %s'%metric_name)
    if subplt is plt :
        subplt.title('Traininig and validation %s'%metric_name)
        subplt.xlabel('Epochs')
        subplt.ylabel(metric_name)
    else :
        subplt.set_title('Traininig and validation %s'%metric_name)
        subplt.set_xlabel('Epochs')
        subplt.set_ylabel(metric_name)
    subplt.legend()
    return subplt

from functools import reduce

def graph_on_train_val(model, history_dict, smooth_curve=False):
    """
    绘制训练损失和验证全部指标
    history = model.fit(...)
    %matplotlib inline
    metric2plt = graph_on_train_val(model, history.history,)
    """
    metrics_names = model.metrics_names
    ncol = len(metrics_names)
    fig, m_axs = plt.subplots(1, ncol, figsize = (20, 3*ncol))
    if not isinstance(m_axs, np.ndarray):
        m_axs = [m_axs]
    def f(i, m):
        plt = graph_on_train_val_metric(history_dict, m, smooth_curve, subplt=m_axs[i])
    list(map(lambda tp:f(*tp), enumerate(metrics_names)))
    return fig
