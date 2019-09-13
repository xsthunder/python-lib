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
