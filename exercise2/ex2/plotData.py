"""用于数据可视化"""
import numpy as np
import matplotlib.pyplot as plt

def plot_data_points(x,y,data_type):
    """画出数据点分布，不同类型用不同颜色"""
    #得到数据的组数
    m = y.size

    x1=[]
    y1=[]
    x2=[]
    y2=[]
    for i in range(m):
        if data_type[i] == 0:
            x1.append(x[i])
            y1.append(y[i])
        else:
            x2.append(x[i])
            y2.append(y[i])
   
    #画图
    plt.scatter(x1,y1,c='yellow',marker='o',edgecolors='black',s=15)
    plt.scatter(x2,y2,c='black',marker='+',edgecolors='black',s=15)

    plt.legend(['Not Admitted','Adimitted'],loc=1)

    plt.show()
