import numpy as np
import matplotlib.pyplot as plt

import plotData
from gradientDescent import *

#加载数据
(x,y)=np.loadtxt('ex1data1.txt',delimiter=',',unpack=True)

#初始参数,学习率,可接受误差，最大迭代次数
ini_theta = np.array([0.0,0.0])
alpha = 0.01
acceptable_err = 1e-6
maxIteration = 10000

#梯度下降
theta_list = gradient_descent(alpha,ini_theta,maxIteration,acceptable_err,x,y)
plotData.plot_regression(theta_list[-1],x,y)
plt.show()
