import numpy as np
def __draw_bar(_m_axs, count_column_name, count, x_label, y_label):
    """
    chinese support @see https://blog.csdn.net/jeff_liu_sky_/article/details/54023745
    """
    _m_axs.set_title(count_column_name, )
    _m_axs.bar(np.arange(len(count)) + 0.5, count)
    _m_axs.set_xticks(np.arange(len(count))+0.5)
    _m_axs.set_xticklabels(count.index)
    _m_axs.set_xlabel(x_label)
    _m_axs.set_ylabel(y_label)
    
    
def draw_bar(_m_axs, count_column_name, sr, threshold=-1, sort_by_index=False, x_label="数值", y_label="记录数"):
    """
    fig, m_axs= plt.subplots(1, 1, figsize = (20, 5))
    draw_bar(m_axs, "apn", sr=df[column_name], threshold=50, sort_by_index=True)
    chinese support @see https://blog.csdn.net/jeff_liu_sky_/article/details/54023745
    """
    count = sr.value_counts()
    if threshold >= 0:
        count = count[count>threshold]
    if sort_by_index: count = count.sort_index()
    __draw_bar(_m_axs, count_column_name, count,  x_label, y_label)