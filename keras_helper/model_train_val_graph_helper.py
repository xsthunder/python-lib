import matplotlib.pyplot as plt

def __smooth_curve(points, factor = 0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous*factor + point*(1-factor))
        else :
            smoothed_points.append(point)
    return smoothed_points

def graph_on_train_val_metric(history_dict, metric, smooth_curve=False):
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

    plt.plot(epochs, metric, 'bo', label='Training %s'%metric_name)
    plt.plot(epochs, val_metric, 'b', label='Validation %s'%metric_name)
    plt.title('Traininig and validation %s'%metric_name)
    plt.xlabel('Epochs')
    plt.ylabel(metric_name)
    plt.legend()
    return plt

from functools import reduce

def graph_on_train_val(model, history_dict, show=True, smooth_curve=False):
    """
    绘制训练损失和验证全部指标，自动展现
    history = model.fit(...)
    %matplotlib inline
    metric2plt = graph_on_train_val(model, history.history,)
    """
    def f(ac, m):
        plt = graph_on_train_val_metric(history_dict, m, smooth_curve)
        if show:
            plt.show()
        ac[m] = plt
        return ac
    ret = reduce(f, model.metrics_names, {})
    return ret

def graph_on_train_val_loss(history_dict):
    """
    绘制训练和验证损失
    history = model.fit(...)
    history_dictt = history.history
    ------
    %matplotlib inline
    plt = graph_on_train_val_loss(history_dict)
    plt.show()
    """
    plt = graph_on_train_val_metric(history_dict, 'loss', smooth_curve)
    return plt

def graph_on_train_val_acc(history_dict,smooth_curve=False):
    """
    绘制训练和验证正确率
    history = model.fit(...)
    history_dictt = history.history
    ------
    %matplotlib inline
    plt = graph_on_train_val_acc(history_dict)
    plt.show()
    """
    plt = graph_on_train_val_metric(history_dict, 'acc', smooth_curve)
    return plt

