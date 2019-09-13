from sklearn import metrics
def draw_auc_roc(fpr, tpr, data=None, title = 'Receiver operating characteristic'):
    """
    from sklearn import metrics
    fpr, tpr, thresholds = metrics.roc_curve(y_true, scores )
    draw_auc_roc(fpr, tpr, data=thresholds)
    """
    roc_auc = metrics.auc(fpr, tpr,)
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc,
            )
    if data is not None:
        for x,y,s in zip(fpr, tpr, data):
            plt.annotate(s, (x,y))
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title )
    plt.legend(loc="lower right")
    plt.show()
    return roc_auc

def draw_roc_of_y_true_cutoffs(y_true_scores, scores, y_true_cutoffs):
    """
    将有标记是全序集合的多分类任务，简化为二分类任务时，需要枚举cutoff，画rocoscore_column_name = 'ECD_信号'
    y_true_scores =df_all['vur-level'] 
    scores = df_all[score_column_name]
    y_true_cutoffs = [1,2,3,4, 5]
    draw_roc_of_y_true_cutoffs(y_true_scores, scores, y_true_cutoffs)
    """
    plt.figure()
    for n in y_true_cutoffs:
        fpr, tpr, thresholds = metrics.roc_curve( y_true_scores>=n,\
                                                 scores) 
        roc_auc = metrics.auc(fpr, tpr,)
        lw = 2
        plt.plot(fpr, tpr, # color='darkorange',
                 lw=lw, label=('ROC curve (area = %0.2f)' % roc_auc + ' vur cutoff %d'%n),
                )
        for x,y,s in zip(fpr, tpr, thresholds): 
            plt.annotate(s, (x,y))
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc="lower right")
    plt.show()
