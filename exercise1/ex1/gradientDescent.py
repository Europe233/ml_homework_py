import numpy as np

from computeCost import *

def next_parameter(alpha,theta,x,y):
    """返回下一步的参数theta"""
    #样本数
    m = x.size
    new_theta = theta.copy()

    #参数迭代
    for i in range(m):
        new_theta[0] = new_theta[0]-alpha*(theta[0]+theta[1]*x[i]-y[i])/m
        new_theta[1] = new_theta[1]-alpha*(theta[0]+theta[1]*x[i]-y[i])*x[i]/m

    return new_theta

def gradient_descent(alpha,ini_theta,maxIteration,acceptable_err,x,y):
    """从初始参数开始迭代，返回一个列表，记录迭代过程中每一步的参数theta"""
    theta_list = []
    theta_list.append(ini_theta)

    #梯度下降
    while True:
        cnt_theta = theta_list[-1]
        next_theta = next_parameter(alpha,cnt_theta,x,y)
        theta_list.append(next_theta)

        #结束条件：超过最大迭代次数 or 误差可接受
        if abs(cost(cnt_theta,x,y)-cost(next_theta,x,y)) < acceptable_err:
            print("迭代次数：",len(theta_list))
            break
        if len(theta_list) > maxIteration:
            print("迭代次数过多！")
            break

    return theta_list


