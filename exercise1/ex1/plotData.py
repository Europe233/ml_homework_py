import numpy as np
import matplotlib.pyplot as plt

def plot_regression(theta,data_x,data_y):
    """根据参数画出拟合的直线"""
     #画出散点图
    plt.scatter(data_x,data_y,c='red',edgecolors='none',s=10)

    #坐标轴设置
    plt.title('Linear Regression',fontsize=20)
    plt.xlabel('Population of City in 10,000s',fontsize=15)
    plt.ylabel('Profit in $10,000s',fontsize=15)

    #画出拟合直线
    x = np.linspace(0,25,100)
    y = theta[0] + theta[1]*x
    plt.plot(x,y,'b')

