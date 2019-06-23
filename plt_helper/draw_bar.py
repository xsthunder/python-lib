import numpy as np
def __draw_bar(_m_axs, count_column_name, count):
    _m_axs.set_title(count_column_name, )
    _m_axs.bar(np.arange(len(count)) + 0.5, count)
    _m_axs.set_xticks(np.arange(len(count))+0.5)
    _m_axs.set_xticklabels(count.index)
    
def draw_bar(_m_axs, count_column_name, sr, threshold=-1, sort_by_index=False):
    """
    fig, m_axs= plt.subplots(1, 1, figsize = (20, 5))
    draw_bar(m_axs, "apn", sr=df[column_name], threshold=50, sort_by_index=True)
    note that count_column_name should be ascii
    """
    count = sr.value_counts()
    if threshold >= 0:
        count = count[count>threshold]
    if sort_by_index: count = count.sort_index()
    __draw_bar(_m_axs, count_column_name, count)