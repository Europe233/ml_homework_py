import numpy as np

def  cost(theta,x,y):
    """计算对应参数的Cost"""
    #数据集样本数
    m = x.size

    #计算cost
    cost = 0
    for i in range(m):
        err = theta[0] + theta[1]*x[i] - y[i]
        cost += (err * err)/ (2 * m)
    return cost
