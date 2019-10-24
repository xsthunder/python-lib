# 初等行变换
import numpy as np
class elementary_matrix:
    """
    https://github.com/xsthunder/python-lib/blob/master/elementary_matrix.py
    """
    def __init__(self, n):
        # 矩阵阶数
        self.NUM_N = n
        
    def row_switch(self, i, j):
        """
        R_i \leftrightarrow R_j
        """
        i -= 1
        j -= 1
        I = np.identity(self.NUM_N).astype(int)
        I[i][i] = 0
        I[j][j] = 0
        I[i][j] = 1
        I[j][i] = 1
        return I

    def row_multiplication(self, i, k):
        """
        kR_i \rightarrow R_i,\ \mbox{where } k \neq 0
        """
        I = np.identity(self.NUM_N)
        if isinstance(k, int):
            I = I.astype(int)
        I[i][i] *= k
        return I

    def row_addition(self, i, j, k):
        """
        R_i + kR_j \rightarrow R_i, \mbox{where } i \neq j
        """
        i -= 1
        j -= 1
        I = np.identity(self.NUM_N)
        if isinstance(k, int):
            I = I.astype(int)
        I[j][i] = k
        return I
