import numpy as np

from plotData import *

# 载入数据，并画出图像
x,y,data_type = np.loadtxt('ex2data1.txt',delimiter=',',usecols=(0,1,2),unpack=True)
print(x)
print(y)
print(data_type)
plot_data_points(x,y,data_type)
